var theme = "dark";

var c_background_dark = '#121212';
var c_font_dark = '#eaeaea';
var c_linksHover_dark = '#ffa42e';
var c_decoration_dark = '#eaeaea';
var font_dark = "Roboto Slab"
var font_wheight_dark  = '400';

var c_background_bright = '#F5F5DC';
var c_font_bright = '#2F4F4F';
var c_linksHover_bright = '#8B0000';
var c_decoration_bright = '#8B4513';
var font_bright = "Roboto Mono"
var font_wheight_bright = '500';

var var_c_background = '--c-background';
var var_c_font = '--c-font';
var var_c_linksHover = '--c-linksHover';
var var_c_decoration = '--c-decoration';
var var_font = '--font';
var var_font_wheight = '--font-wheight';



function setCSSVariable(variableName, value, element = document.documentElement) {
    element.style.setProperty(variableName, value);
    localStorage.setItem(variableName, value);
}

function styleBright() {
    setCSSVariable(var_c_background, c_background_bright);
    setCSSVariable(var_c_font, c_font_bright);
    setCSSVariable(var_c_linksHover, c_linksHover_bright);
    setCSSVariable(var_c_decoration, c_decoration_bright);
    setCSSVariable(var_font, font_bright);
    setCSSVariable(var_font_wheight, font_wheight_bright);

    theme = "bright";
}

function styleDark() {
    setCSSVariable(var_c_background, c_background_dark);
    setCSSVariable(var_c_font, c_font_dark);
    setCSSVariable(var_c_linksHover, c_linksHover_dark);
    setCSSVariable(var_c_decoration, c_decoration_dark);
    setCSSVariable(var_font, font_dark);
    setCSSVariable(var_font_dark, font_wheight_dark);

    theme = "dark";
}

function applySavedCSSVariables(element = document.documentElement) {
    for (let i = 0; i < localStorage.length; i++) {
        const variableName = localStorage.key(i);
        const value = localStorage.getItem(variableName);
        element.style.setProperty(variableName, value);
    }
}

// Anwenden der gespeicherten Variablen beim Laden der Seite
document.addEventListener('DOMContentLoaded', () => {
    applySavedCSSVariables();
});