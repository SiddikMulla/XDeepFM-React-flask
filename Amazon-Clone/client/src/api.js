const axios = require('axios')

async function fetchData() {
    const username = 'Siddik';
    const password = 'Siddik_1234MM';
    const body = {
        'source': 'amazon_product',
        'domain': 'com',
        'query': 'B0719X5WJ5',
        'parse': true,
        'context': [
            {'key': 'autoselect_variant', 'value': false},
        ],
    };

    try {
        const response = await axios.post('https://realtime.oxylabs.io/v1/queries', body, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + Buffer.from(`${username}:${password}`).toString('base64'),
            }
        });

        console.log(JSON.stringify(response.data, null, 2)); // Convert response.data to JSON string
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

fetchData();
