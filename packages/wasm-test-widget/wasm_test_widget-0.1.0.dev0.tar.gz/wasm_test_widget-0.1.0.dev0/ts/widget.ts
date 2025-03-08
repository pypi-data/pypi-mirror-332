import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from "@jupyter-widgets/base";
import WGPUApp from "./cpp/wgpu_app";
import { MODULE_NAME, MODULE_VERSION } from "./version";

export class WasmWidgetModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: WasmWidgetModel.model_name,
      _model_module: WasmWidgetModel.model_module,
      _model_module_version: WasmWidgetModel.model_module_version,
      _view_name: WasmWidgetModel.view_name,
      _view_module: WasmWidgetModel.view_module,
      _view_module_version: WasmWidgetModel.view_module_version,
      // Message to send back and forth for testing/example
      message: null as string,
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
    // Add any extra serializers here
  };

  // TODO: must match Python
  static model_name = "WasmWidgetModel";
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = "WasmWidgetView";
  static view_module = MODULE_NAME;
  static view_module_version = MODULE_VERSION;
}

export class WasmWidgetView extends DOMWidgetView {
  static next_canvas_id = 0;
  canvas: HTMLCanvasElement;

  // Called when the widget is displayed
  render() {
    const canvas = document.createElement("canvas");
    this.canvas = canvas;
    // TODO: these params should be set when making the widget
    canvas.width = 640;
    canvas.height = 480;
    // TODO: my webgpu thing doesn't take the canvas name to use
    canvas.id = "canvas";
    //canvas.id = `canvas-${WasmWidgetModel.view_name}-${WasmWidgetView.next_canvas_id}`;

    WasmWidgetView.next_canvas_id += 1;

    this.el.appendChild(canvas);
    console.log("mounted");

    // We need to wait for the canvas element to be added before
    // we can set up the canvas so wait for a frame
    requestAnimationFrame(async () => {
      // Get a GPU device to render with
      const adapter = await navigator.gpu.requestAdapter();
      const device = await adapter.requestDevice();

      console.log(adapter);
      console.log(device);
      console.log(canvas);

      // We set -sINVOKE_RUN=0 when building and call main ourselves because something
      // within the promise -> call directly chain was gobbling exceptions
      // making it hard to debug
      const app = await WGPUApp({
        preinitializedWebGPUDevice: device,
        canvas,
      });

      try {
        app.callMain();
      } catch (e) {
        console.error(e.stack);
      }
    });
  }
}
