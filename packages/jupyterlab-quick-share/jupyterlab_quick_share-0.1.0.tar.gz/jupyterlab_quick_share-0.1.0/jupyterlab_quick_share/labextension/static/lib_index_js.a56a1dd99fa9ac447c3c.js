"use strict";
(self["webpackChunkjupyterlab_quick_share"] = self["webpackChunkjupyterlab_quick_share"] || []).push([["lib_index_js"],{

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   requestAPI: () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'jupyterlab-quick-share', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");



const plugin = {
    id: 'jupyterlab-quick-share:plugin',
    description: 'Send/receive links that make it easy to share notebooks (and other files)',
    autoStart: true,
    requires: [_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_0__.IDefaultFileBrowser, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__.ISettingRegistry],
    activate: async (app, fileBrowser, settingRegistry) => {
        console.log('JupyterLab extension jupyterlab-quick-share is activated!');
        const settings = (await settingRegistry.load(plugin.id)).composite.private;
        if (settings.enableJupytextIssue1344Fix) {
            fixJupytextIssue1344(app);
        }
        app.commands.addCommand('jupyterlab-quick-share:share', {
            label: '⚡️ Copy Quick Share Link',
            execute: async () => {
                // TODO: Error if not a single file
                const selectedFile = fileBrowser.selectedItems().next().value;
                // console.log('Selected file:', selectedFile);
                const data = await (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)(`share?path=${encodeURIComponent(selectedFile.path)}`);
                await navigator.clipboard.writeText(data.url);
                // console.log('copied to clipboard:', data.url);
            }
        });
        app.contextMenu.addItem({
            command: 'jupyterlab-quick-share:share',
            selector: '.jp-DirListing-item[data-isdir="false"]',
            rank: 0
        });
    }
};
function fixJupytextIssue1344(app) {
    app.shell.layoutModified.connect(() => {
        // query for an element with class jp-Launcher-sectionTitle and innerText "Jupytext"
        const jupytextSectionTitle = Array.from(document.querySelectorAll('.jp-Launcher-sectionTitle'))
            .find(el => { var _a; return ((_a = el.textContent) === null || _a === void 0 ? void 0 : _a.trim()) === "Jupytext"; });
        if (jupytextSectionTitle) {
            const jupytextSection = jupytextSectionTitle.closest('.jp-Launcher-section');
            console.log("jupytextSection:", jupytextSection);
            // jupytextSection?.remove();
        }
        // document.querySelector('.jp-Launcher-section')?.remove();
    });
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.a56a1dd99fa9ac447c3c.js.map