/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'selector',
    content: [
      "./pages/**/*.{js,jsx,ts,tsx,md,mdx}",
      "./components/**/*.{js,jsx,ts,tsx,md,mdx}",
  
      // Or if using `src` directory:
      "./src/**/*.{js,jsx,ts,tsx,md,mdx}",
    ],
    theme: {
      extend: {
        colors: {
          primary: {
            DEFAULT: "hsl(var(--primary))",
            foreground: "hsl(var(--primary-foreground))",
          },
          secondary: {
            DEFAULT: "hsl(var(--secondary))",
            foreground: "hsl(var(--secondary-foreground))",
          },
        },
      },
    },
    plugins: [],
  };