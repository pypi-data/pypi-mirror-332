const path = require("path");

const rules = [
  {
    test: /\.(png|jpg|jpeg|glb)$/i,
    type: "asset/resource",
  },
  {
    test: /\.wasm$/i,
    type: "asset/resource",
  },
  {
    test: /\.tsx?$/,
    use: "ts-loader",
    exclude: /node_modules/,
  },
];

const resolve = {
  extensions: [".tsx", ".ts", ".js"],
};

const externals = ["@jupyter-widgets/base"];

module.exports = [
  /* Notebook extension.
   *
   * This contains the JS that's run on load of the notebook
   */
  {
    entry: "./ts/extension.ts",
    mode: "development",
    devtool: "inline-source-map",
    output: {
      filename: "index.js",
      path: path.resolve(__dirname, "wasm_test_widget", "nbextension"),
      libraryTarget: "amd",
      publicPath: "",
    },
    module: {
      rules,
    },
    resolve,
    externals,
  },

  /* Embeddable widget bundle
   *
   * This contains the static assets and other frontend only widget code
   */
  {
    entry: "./ts/index.ts",
    mode: "development",
    devtool: "inline-source-map",
    output: {
      filename: "index.js",
      path: path.resolve(__dirname, "dist"),
      libraryTarget: "amd",
      library: "wasm_test_widget",
    },
    module: {
      rules,
    },
    resolve,
    externals,
  },
];
