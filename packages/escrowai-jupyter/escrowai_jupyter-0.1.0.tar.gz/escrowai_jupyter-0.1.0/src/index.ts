import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ICommandPalette } from '@jupyterlab/apputils';

/**
 * Initialization data for the escrowai-jupyter extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'escrowai-jupyter:plugin',
  description: 'An extension to encrypt and upload the working directory to EscrowAI',
  autoStart: true,
  optional: [ICommandPalette],
  activate: (app: JupyterFrontEnd, palette: ICommandPalette | null) => {
    console.log('JupyterLab extension escrowai-jupyter is activated!');
    const command = 'escrowai-jupyter:run-script'
    app.commands.addCommand(command, {
      label: 'Upload to EscrowAI',
      execute: async () => {
        const response = await fetch('/escrowai-jupyter/run-script');
        const text = await response.text();
        console.log(text);
      }  
    });
    if (palette) {
      palette.addItem({ command, category: 'Extensions' });
    }
  }
};

export default plugin;
