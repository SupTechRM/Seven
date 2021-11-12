const { app, BrowserWindow } = require('electron')

function createWindow() {
    const win = new BrowserWindow({
        width: 1366,
        height: 780
    })

    win.loadFile('setup/setupUi_Main/presentation.html')
}

app.whenReady().then(() => {
    createWindow()
})