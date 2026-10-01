import manifest from './photo-manifest.json';

export type Category = 'outdoors' | 'living' | 'rooms' | 'sauna';

export interface Photo {
  id: number;
  alt: string;
  category: Category;
  w: number;
  h: number;
  color: string;
}

const meta: Record<number, [Category, string]> = {
  1: ['outdoors', 'The wooden cabin and its long natural pool, seen from the lawn'],
  2: ['outdoors', 'The natural pool with the wooded valley behind it'],
  3: ['outdoors', 'The pool running along the covered terrace'],
  4: ['outdoors', 'The covered outdoor kitchen behind the pool deck'],
  5: ['outdoors', 'A wooden walkway along the pool, looking out over the valley'],
  6: ['outdoors', 'The dark timber cabin with orange shutters above the pool'],
  7: ['outdoors', 'Roses beside the pool with the cabin in the background'],
  8: ['outdoors', 'The pool and cabin in the sun, with the mountains beyond'],
  9: ['living', 'The open living area with a wooden table and the wood-burning stove'],
  10: ['living', 'The modern kitchen with oven, gas hob and microwave'],
  11: ['living', 'The living area, wood stove and dining table'],
  12: ['living', 'The fully equipped kitchen with a wooden bench'],
  13: ['living', 'The wood-burning stove, a stack of logs and the sofa'],
  14: ['living', 'The sofa and coffee table in front of the stove'],
  15: ['living', 'Open-plan living, dining and kitchen under a wooden ceiling'],
  16: ['rooms', 'The downstairs bathroom with a heated towel rail'],
  17: ['rooms', 'The walk-in shower on the ground floor'],
  18: ['rooms', 'A bedroom with a double bed, wardrobe and warm wooden walls'],
  19: ['rooms', 'A bedroom with a double bed and a single bed under the window'],
  21: ['rooms', 'A single bed under a low window in the bedroom'],
  22: ['rooms', 'The upstairs half-bath, all in wood'],
  23: ['rooms', 'The second bedroom with a double bed and a sloping window'],
  24: ['rooms', 'A small desk and a double bed in the second bedroom'],
  25: ['rooms', 'A triangular window with a view of the mountains'],
  26: ['rooms', 'The second bedroom under the exposed roof beams'],
  27: ['sauna', 'The sauna, softly lit'],
  28: ['sauna', 'The sauna stove with stones and a wooden bucket'],
  29: ['outdoors', 'The front door with an old cowbell'],
  30: ['outdoors', 'The brick pizza oven in the outdoor kitchen'],
  31: ['outdoors', 'The outdoor kitchen with sink, fridge, cooker and pizza oven'],
  32: ['outdoors', 'The long dining table under the covered terrace, with a dartboard'],
  33: ['outdoors', 'Two folding chairs and a glass of wine on the grass'],
  34: ['outdoors', 'The cabin seen from the meadow above'],
  35: ['outdoors', 'The picnic area with a fire pit, under the trees'],
  36: ['outdoors', 'A small waterfall and clear pool in the stream'],
};

export const photos: Record<number, Photo> = Object.fromEntries(
  Object.entries(meta).map(([id, [category, alt]]) => {
    const m = (manifest as Record<string, { w: number; h: number; color: string }>)[id];
    return [id, { id: Number(id), alt, category, w: m.w, h: m.h, color: m.color }];
  }),
);

export const gallery: Photo[] = Object.values(photos);

/** srcset for one photo; widths match scripts/optimize-photos.py */
export function srcset(id: number) {
  return [640, 1280, 1920].map((w) => `/img/${id}-${w}.webp ${w}w`).join(', ');
}
export const src = (id: number, w: 640 | 1280 | 1920 = 1280) => `/img/${id}-${w}.webp`;
