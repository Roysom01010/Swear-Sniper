let foulWords = [];

// Load data with error handling
document.getElementById('loading').classList.remove('hidden');
fetch('https://raw.githubusercontent.com/Roysom01010/Swear-Sniper/main/foul-words.json')
  .then(response => {
    if (!response.ok) throw new Error('Network error');
    return response.json();
  })
  .then(data => {
    foulWords = data.filter(item => item.A && item.A.trim() !== '');
    populateFilters();
  })
  .catch(error => {
    console.error('Fetch error:', error);
    document.getElementById('error').textContent = 'Failed to load word list';
  })
  .finally(() => document.getElementById('loading').classList.add('hidden'));
