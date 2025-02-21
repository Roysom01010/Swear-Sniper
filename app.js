let foulWords = [];

// Load foul words data
fetch('foul-words.json')
    .then(response => response.json())
    .then(data => {
        foulWords = data;
        populateFilters();
    });

function populateFilters() {
    // Populate languages
    const languages = [...new Set(foulWords.map(item => item['what is language of the keyword']))];
    populateMultiSelect('languageSelect', languages.filter(Boolean));

    // Populate age ratings
    const ratings = [...new Set(foulWords.map(item => item['Minimum Rating Band']))];
    populateSelect('ageRating', ratings.filter(Boolean));

    // Populate Content Descriptor Values (Language Types)
    const contentDescriptors = [...new Set(foulWords.map(item => item['Content Descriptor Value']))];
    populateMultiSelect('languageType', contentDescriptors.filter(Boolean));
}

function populateSelect(elementId, options) {
    const select = document.getElementById(elementId);
    select.innerHTML = ''; // Clear existing options
    options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option;
        select.appendChild(opt);
    });
}

function populateMultiSelect(elementId, options) {
    const select = document.getElementById(elementId);
    select.innerHTML = ''; // Clear existing options
    options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option;
        select.appendChild(opt);
    });
}

document.getElementById('runButton').addEventListener('click', () => {
    const script = document.getElementById('scriptInput').value;
    const selectedLanguages = Array.from(document.getElementById('languageSelect').selectedOptions)
        .map(opt => opt.value);
    const selectedAgeRating = document.getElementById('ageRating').value;
    const selectedLanguageTypes = Array.from(document.getElementById('languageType').selectedOptions)
        .map(opt => opt.value);

    // Filter words based on selections
    const filteredWords = foulWords.filter(word => {
        return (
            (!selectedLanguages.length || selectedLanguages.includes(word['what is language of the keyword'])) &&
            (!selectedAgeRating || word['Minimum Rating Band'] === selectedAgeRating) &&
            (!selectedLanguageTypes.length || selectedLanguageTypes.includes(word['Content Descriptor Value']))
        );
    });

    // Find matches with improved regex
    const results = {};
    filteredWords.forEach(word => {
        const regex = new RegExp(`(^|\\s)${word.Keyword}(?=\\s|$)`, 'gi');
        const matches = script.match(regex);
        if (matches) {
            results[word.Keyword] = matches.length;
        }
    });

    // Display results
    displayResults(results);
});

function displayResults(results) {
    const total = Object.values(results).reduce((a, b) => a + b, 0);
    document.getElementById('wordCount').innerHTML = `
        <strong>Total flagged words: ${total}</strong>
    `;

    const wordsList = Object.entries(results).map(([word, count]) => `
        <div class="word-item">
            <span>${word}:</span>
            <span>${count} occurrences</span>
        </div>
    `).join('');

    document.getElementById('flaggedWords').innerHTML = wordsList || '<div>No foul language detected!</div>';
}
