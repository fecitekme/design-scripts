/*
 * Script by Arif Furkan Karaca
 * Website: fecitekme.com | Email: arifkaraca@protonmail.com
 * Thanks for using this script. Let's streamline your design imports.
 */

// Polyfill for Object.keys for older JavaScript environments
// Ensures compatibility with older systems that lack Object.keys.

if (!Object.keys) {
    Object.keys = (function () {
        'use strict';
        var hasOwnProperty = Object.prototype.hasOwnProperty,
            hasDontEnumBug = !({toString: null}).propertyIsEnumerable('toString'),
            dontEnums = [
                'toString',
                'toLocaleString',
                'valueOf',
                'hasOwnProperty',
                'isPrototypeOf',
                'propertyIsEnumerable',
                'constructor'
            ],
            dontEnumsLength = dontEnums.length;

        return function (obj) {
            if (typeof obj !== 'object' && (typeof obj !== 'function' || obj === null)) {
                throw new TypeError('Object.keys called on non-object');
            }

            var result = [], prop, i;

            for (prop in obj) {
                if (hasOwnProperty.call(obj, prop)) {
                    result.push(prop);
                }
            }

            if (hasDontEnumBug) {
                for (i = 0; i < dontEnumsLength; i++) {
                    if (hasOwnProperty.call(obj, dontEnums[i])) {
                        result.push(dontEnums[i]);
                    }
                }
            }

            return result;
        };
    }());
}

// Polyfill for JSON.stringify for older JavaScript environments
// Ensures JSON functions are available, even in older systems.

if (typeof JSON === 'undefined') {
    JSON = {
        stringify: function (obj) {
            var t = typeof (obj);
            if (t !== "object" || obj === null) {
                // Converts basic types to JSON.
                if (t === "string") obj = '"' + obj.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"';
                return String(obj);
            } else {
                // Converts arrays and objects to JSON.
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

// Custom JSON Loader Function using eval
// Loads and parses a JSON file, updating Illustrator with the content.

function loadCustomTextFromJSON(filePath) {
    var file = new File(filePath);
    file.encoding = "UTF8";
    if (!file.exists) {
        $.writeln("Custom JSON file not found!");
        return null;
    }

    $.writeln("Opening custom JSON file: " + filePath);
    file.open("r");
    var jsonData = file.read();
    file.close();

    $.writeln("Custom JSON Data Length: " + jsonData.length);

    try {
        var parsedData = eval('(' + jsonData + ')'); // Parses the JSON string.
        $.writeln("Custom JSON parsed successfully.");
        return parsedData;
    } catch (error) {
        $.writeln("Error parsing custom JSON: " + error.message);
        $.writeln("Custom JSON Data: " + jsonData);
        return null;
    }
}

// Custom Import Function to Update Text Frames
// Updates text frames in Illustrator with the loaded JSON content.

function importCustomTranslatedTexts() {
    var doc = app.activeDocument;
    $.writeln("Starting custom import process...");

    // Get the current script's folder.
    var scriptFile = new File($.fileName);
    var scriptFolder = scriptFile.path;

    // Construct the file path assuming it's in the same folder as the script.
    var jsonFile = new File(scriptFolder + "/translated_large_file.json");

    if (jsonFile.exists) {
        $.writeln("Custom JSON file selected: " + jsonFile.fsName);
        var translatedTexts = loadCustomTextFromJSON(jsonFile);

        if (!translatedTexts) {
            $.writeln("Failed to load or parse custom JSON data.");
            return;
        }

        $.writeln("Loaded custom JSON data successfully.");
        $.writeln("Custom JSON structure: " + JSON.stringify(translatedTexts, null, 4));

        var textFrames = doc.textFrames;
        $.writeln("Total custom text frames found: " + textFrames.length);

        for (var i = 0; i < textFrames.length; i++) {
            var customFrameKey = "custom_frame_" + i;
            $.writeln("Processing " + customFrameKey);

            if (translatedTexts[doc.name] && translatedTexts[doc.name][customFrameKey]) {
                var paragraphs = translatedTexts[doc.name][customFrameKey];
                $.writeln("Type of custom paragraphs: " + typeof paragraphs);

                if (paragraphs && typeof paragraphs === 'object') {
                    var newContents = "";

                    for (var j = 0; j < Object.keys(paragraphs).length; j++) {
                        var customParagraphKey = "custom_paragraph_" + j;
                        $.writeln("Processing " + customParagraphKey);

                        if (paragraphs[customParagraphKey] && paragraphs[customParagraphKey].custom_content) {
                            var content = String(paragraphs[customParagraphKey].custom_content);
                            newContents += content + "\r";
                        } else {
                            newContents += "\r";  // Preserve line breaks for empty paragraphs.
                            $.writeln("Empty line preserved for " + customParagraphKey);
                        }
                    }

                    textFrames[i].contents = newContents;
                    $.writeln("Updated custom frame " + i + " with new contents.");
                } else {
                    $.writeln("Error: custom paragraphs is not a plain object.");
                }
            } else {
                $.writeln("No matching content found for custom frame " + i);
            }
        }

        alert("Successfully imported custom translated texts and updated the document.");
    } else {
        $.writeln("No custom JSON file found in the expected location: " + jsonFile.fsName);
    }
}

// Run the custom import function
// Updates the document with the translated content.
importCustomTranslatedTexts();
