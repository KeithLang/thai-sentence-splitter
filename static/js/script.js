document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('splitForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const sentence = document.getElementById('thaiSentence').value;

        try {
            const response = await fetch('/split', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ sentence }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            displayResult(data.words);
        } catch (error) {
            console.error('Error:', error);
            resultDiv.innerHTML = '<p class="text-danger">An error occurred while processing your request.</p>';
        }
    });

    function displayResult(words) {
        resultDiv.innerHTML = '';
        words.forEach(word => {
            const wordSpan = document.createElement('span');
            wordSpan.className = 'word';
            wordSpan.textContent = word;
            resultDiv.appendChild(wordSpan);
        });
    }
});
