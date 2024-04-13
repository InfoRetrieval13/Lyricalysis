/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
    theme: {
        extend: {
            fontFamily: {
                inter: ["Inter", "sans-serif"],
                righteous: ["Righteous", "cursive"],
                roboto: ["Roboto", "sans-serif"],
                lora: ["Lora", "serif"],
                poppins: ["Poppins", "sans-serif"],
            },
            colors: {
                grey: "#585563",
                violet: "#5B2E48",
                bluey: "#6883BA",
                greeny: "#18A999",
                redy: "#8C271E",
                whitey: "#F9F9F9",
                dbluey: "#153243",
                dredy: "#AD343E",
            },
        },
    },
    plugins: [],
};
