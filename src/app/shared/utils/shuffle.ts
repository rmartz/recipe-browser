export function shuffle<T>(items: T[]): T[] {
  // Implementation of Fisher Yates shuffle algorithm, adapted from Mike Bostock
  // https://bost.ocks.org/mike/shuffle/
  let m = items.length;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    const i = Math.floor(Math.random() * m);
    m -= 1;

    // And swap it with the current element.
    const t = items[m];
    items[m] = items[i];
    items[i] = t;
  }

  return items;
}
