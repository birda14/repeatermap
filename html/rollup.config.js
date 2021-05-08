import { terser } from "rollup-plugin-terser";

export default {
  input: "scripts/index.js",
  output: [
    {
      file: "_site/bundle.js",
      format: "iife",
      sourcemap: true,
      plugins: [terser()],
    },
  ],
};