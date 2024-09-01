var values_dark = [
    '#121212', 
    '#eaeaea', 
    '#ffa42e',
    '#eaeaea',
    "Roboto Slab",
    '400',
    '1.5',
    '1.4px',
    'normal',
];

var values_bright = [
    '#f7f7e9',
    '#2F4F4F',
    '#8B0000',
    '#8B4513',
    "Roboto Mono",
    '500',
    '1.5',
    '0.5px',
    '-5.5px'
];

var value_names = [
    '--c-background',
    '--c-font',
    '--c-linksHover',
    '--c-decoration',
    '--font',
    '--font-wheight',
    '--line-height',
    '--letter-spacing',
    '--word-spacing',
];




function setCSSVariable(variableName, value, element = document.documentElement) {
    element.style.setProperty(variableName, value);
    localStorage.setItem(variableName, value);
}

function styleBright() {
    if (value_names.length == values_bright.length) {
        for(var i = 0; i<value_names.length; i++)  {
            setCSSVariable(value_names[i], values_bright[i]);
        }
    } else {
        console.log("EIne css refernez in einer der Arrays wurde vergessen in style.css")
    }
}

function styleDark() {
    if (value_names.length == values_dark.length) {
        for(var i = 0; i<value_names.length; i++)  {
            setCSSVariable(value_names[i], values_dark[i]);
        }
    } else {
        console.log("EIne css refernez in einer der Arrays wurde vergessen in style.css")
    }
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

var overlay = document.getElementById("id-overlay");

function toggleOverlay(event){
    if (document.getElementById("id-overlay").style.display == 'flex') {
        document.getElementById("id-overlay").style.display = 'none'; 
    } else {
        document.getElementById("id-overlay").style.display = 'flex'; 
        var image = event.target;
        document.getElementById("id-image-fullsize").src= image.src; 
    }
}

