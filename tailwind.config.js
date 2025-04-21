module.exports = {
    content: [
      "./templates/**/*.html",   // All HTML files inside templates folder
      // you can add other paths if necessary
    ],
    theme: {
      extend: {},
    },
    plugins: [
      require('@tailwindcss/typography'),
    ],
  };
  