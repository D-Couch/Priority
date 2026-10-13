// Normalize only references to sources actually supplied with this answer.
// This changes presentation, never the stored model answer or its review grade.
export function linkableCitations(text, sources) {
  const ids = new Set(sources.map(source => source.id));
  return text.replace(/\[(?:CR \d{3}(?:\.\d+[a-z]?)?|MTR \d+\.\d+|C\d+)\]|\b(?:(?:CR|[Rr]ule)\s+)?(\d{3}\.\d+[a-z]?)\b/g,
    (match, number) => number && ids.has(`CR ${number}`) ? `[CR ${number}]` : match);
}
