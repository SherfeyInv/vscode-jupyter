// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
'use strict';

let messageLogger: undefined | ((message: string) => void);
export function logMessage(message: string) {
    if (messageLogger) {
        messageLogger(message);
    }
}
/**
 * Logging in production seems to slow down webview (unnecessarily too chatty)
 */
export function logMessageOnlyOnCI(message: string) {
    // TODO: No way to check if CI for webview
    if (messageLogger) {
        messageLogger(message);
    }
}

export function setLogger(logger: (message: string) => void) {
    messageLogger = logger;
}