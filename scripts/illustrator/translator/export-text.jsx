/*
 * Script by Arif Furkan Karaca
 * Website: fecitekme.com | Email: arifkaraca@protonmail.com
 * Thanks for using this script. Let's make your workflow smoother.
 */

// JSON Polyfill for ExtendScript environments
// Ensuring this script works even in older or limited systems.

if (typeof JSON === 'undefined') {
    JSON = {
        stringify: function (obj) {
            var t = typeof (obj);
            if (t !== "object" || obj === null) {
                // Handles basic data types.
                if (t === "string") obj = '"' + obj.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"';
                return String(obj);
            } else {
                // Handles arrays and objects.
                var n, v, json = [], arr = (obj && obj.constructor === Array);
                for (n in obj) {
                    v = obj[n];
                    t = typeof (v);
                    if (t === "string") v = '"' + v.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"';
                    else if (t === "object" && v !== null) v = JSON.stringify(v);
                    json.push((arr ? "" : '"' + n + '":') + String(v));
                }
                return (arr ? "[" : "{") + String(json) + (arr ? "]" : "}");
            }
        }
    };
}

// Exporter: Custom JSON Text Exporter for Illustrator
// Handles the export of text frames to a JSON file.

function customEscapeString(str) {
    return str.replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\n/g, "\\n").replace(/\r/g, "\\r");
}

// Custom Export Function for Paragraph Texts
// Exports paragraph text data from Illustrator to a structured JSON file.

function exportCustomTextsAsJSON() {
    var doc = app.activeDocument;
    var customExportData = {};
    customExportData[doc.name] = {};

    for (var i = 0; i < doc.textFrames.length; i++) {
        var textFrame = doc.textFrames[i];
        var customFrameKey = "custom_frame_" + i;
        customExportData[doc.name][customFrameKey] = {};

        var paragraphs = textFrame.contents.split('\r');
        for (var j = 0; j < paragraphs.length; j++) {
            var customParagraphKey = "custom_paragraph_" + j;
            customExportData[doc.name][customFrameKey][customParagraphKey] = {
                "custom_content": customEscapeString(paragraphs[j])
            };
        }
    }

    var saveFile = File.saveDialog("Save the custom export JSON file", "*.json");
    if (saveFile) {
        saveFile.open("w");
        saveFile.encoding = "UTF8";
        saveFile.write(JSON.stringify(customExportData, null, 4));
        saveFile.close();
        alert("Custom text data has been exported successfully.");
    }
}

// Initiate the custom export process.
exportCustomTextsAsJSON();
