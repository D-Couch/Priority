"""Decode LM Studio streams without storing or displaying private reasoning."""
import json


class VisibleText:
    def __init__(self):
        self.pending = ''
        self.thinking = False
        self.hidden_characters = 0

    def feed(self, chunk):
        self.pending += chunk
        visible = []
        while self.pending:
            tag = '</think>' if self.thinking else '<think>'
            index = self.pending.find(tag)
            if index >= 0:
                text = self.pending[:index]
                if self.thinking:
                    self.hidden_characters += len(text)
                else:
                    visible.append(text)
                self.pending = self.pending[index + len(tag):]
                self.thinking = not self.thinking
            else:
                keep = next((n for n in range(min(len(tag)-1,len(self.pending)),0,-1)
                             if self.pending.endswith(tag[:n])),0)
                text = self.pending[:-keep] if keep else self.pending
                if self.thinking:
                    self.hidden_characters += len(text)
                else:
                    visible.append(text)
                self.pending = self.pending[-keep:] if keep else ''
                break
        return ''.join(visible)

    def finish(self):
        text = '' if self.thinking else self.pending
        if self.thinking:
            self.hidden_characters += len(self.pending)
        self.pending = ''
        return text


def decode_completion(upstream):
    visible = VisibleText()
    stats = {'finish_reason':None, 'usage':None, 'reasoning_characters':0,
             'visible_characters':0, 'stream_completed':False}
    for raw in upstream:
        line = raw.decode('utf-8').strip()
        if not line.startswith('data:'):
            continue
        data = line[5:].strip()
        if data == '[DONE]':
            stats['stream_completed'] = True
            break
        event = json.loads(data)
        if event.get('error'):
            error = event['error']
            raise RuntimeError(error.get('message','LM Studio generation failed') if isinstance(error,dict) else str(error))
        if event.get('usage'):
            stats['usage'] = event['usage']
        for choice in event.get('choices',[]):
            if choice.get('index',0) != 0:
                continue
            stats['finish_reason'] = choice.get('finish_reason') or stats['finish_reason']
            delta = choice.get('delta',{})
            stats['reasoning_characters'] += len(delta.get('reasoning_content') or delta.get('reasoning') or '')
            text = visible.feed(delta.get('content') or '')
            if text:
                stats['visible_characters'] += len(text)
                yield {'type':'token','text':text}
    text = visible.finish()
    if text:
        stats['visible_characters'] += len(text)
        yield {'type':'token','text':text}
    stats['reasoning_characters'] += visible.hidden_characters
    yield {'type':'diagnostics', **stats}
    if not stats['stream_completed']:
        raise RuntimeError('LM Studio stream ended without a completion marker')
