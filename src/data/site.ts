// One place for the facts that appear all over the site.
// Anything marked TODO is a placeholder that still needs a real value.

export const site = {
  name: 'Guest House Poleska',
  tagline: 'A one-of-a-kind wooden cabin on a natural pool, in the mountains of Montenegro.',
  place: 'Opasanica, Komovi, Montenegro',

  guests: 6,
  bedrooms: 2,
  areaM2: 80,
  poolLengthM: 23,
  priceFrom: 85, // euro per night
  saunaSupplement: 15, // euro, must be booked in advance

  airbnbUrl: 'https://www.airbnb.com/rooms/1776275231628249640',
  // Neighbours' family restaurant in Opasanica (Sladja).
  restaurant: { name: 'Sladjina tradicionalna kuhinja', url: 'https://maps.app.goo.gl/V7THn4hhLLjPmy8bA' },
  instagramUrl: 'https://www.instagram.com/guesthousepoleska/',
  instagramHandle: '@guesthousepoleska',

  // Hospitable direct-booking widget (shown on the Book page).
  hospitable: {
    siteUuid: 'a2cc3de3-43fd-49d9-b3af-d908aed2e11f',
    propertyId: '2498157',
    theme: 'multi',
  },

  // No email address is shown on the site: visitors use the contact form.
  whatsapp: '', // e.g. '+38269000000'; leave empty to hide the WhatsApp link
  // TODO: paste the endpoint of a form service (Formspree, Web3Forms, ...) here. The service
  // forwards each message to the hosts' inbox, so the address itself never appears on the site.
  // While empty, the form runs in test mode and sends nothing.
  formEndpoint: '',
};

export const nav = [
  { href: '/cabin/', label: 'The cabin' },
  { href: '/outdoors/', label: 'Pool & outdoors' },
  { href: '/explore/', label: 'Explore' },
  { href: '/book/', label: 'Book' },
  { href: '/contact/', label: 'Contact' },
];
