// main.js - FIXED for packaged Electron apps
const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 1400,
    height: 900,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true
    }
  });

  // ✅ FIXED: Use correct path for packaged vs dev
  const indexPath = path.join(__dirname, 'index.html');
  win.loadFile(indexPath);
  
  // ✅ DISABLE DEVTOOLS in production builds
  if (process.env.NODE_ENV === 'production') {
    win.webContents.on('devtools-opened', () => {
      win.webContents.closeDevTools();
    });
  }
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
