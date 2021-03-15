/**
 * Global Styles Plugin
 *
 * This plugin modifies Tailwind’s base styles using values from the theme.
 * https://tailwindcss.com/docs/adding-base-styles#using-a-plugin
 */
const globalStyles = ({ addBase, config }) => {
    addBase({
        a: {
            color: config('theme.colors.brand.red'),
        },
        'a:hover': {
            textDecoration: 'underline',
        },
        p: {
            marginBottom: config('theme.margin.3'),
            lineHeight: config('theme.lineHeight.normal'),
        },
        'h1, h2, h3, h4, h5': {
            marginBottom: config('theme.margin.2'),
            lineHeight: config('theme.lineHeight.tight'),
        },
        h1: { fontSize: config('theme.fontSize.5xl') },
        h2: { fontSize: config('theme.fontSize.4xl') },
        h3: { fontSize: config('theme.fontSize.3xl') },
        h4: { fontSize: config('theme.fontSize.2xl') },
        h5: { fontSize: config('theme.fontSize.xl') },
        'ol, ul': { paddingLeft: config('theme.padding.4') },
        ol: { listStyleType: 'decimal' },
        ul: { listStyleType: 'disc' },
    });
}

/**
 * Configuration
 */
module.exports = {
    purge: {
        enabled: false,
        layers: ['components', 'utilities'],
        content: ['_site/**/*.html'],
        options: {
            safelist: [],
        },
    },
    theme: {
        screens: {
            sm: '480px',
            md: '768px',
            lg: '976px',
            xl: '1440px',
        },
        colors: {
            brand: {
                red: '#ff0000',
            },
            white: '#ffffff',
            black: '#232222',
            gray: {
                50: '#fcfcfc',
                100: '#f8f8f8',
                200: '#eeeeee',
                300: '#e4e4e4',
                400: '#cfd0d0',
                500: '#bbbcbc',
                600: '#a8a9a9',
                700: '#8c8d8d',
                800: '#707171',
                900: '#5c5c5c'
            },
            transparent: 'transparent',
        },
    },
    variants: {},
    plugins: [
        globalStyles
    ],
}