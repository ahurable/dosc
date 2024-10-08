/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/*.html',
    './**/**/*.html',
    './templates/**/*.html'
  ],
  theme: {
    container:{
      center: true,
      screens: {
        sm: '105.62180579216354vh',
        md: '122.65758091993186vh',
        lg: '151.618398637138vh',
        xl: '187.39352640545144vh'
      }
    },
    extend: {
      
    },
  },
  plugins: [],
}

