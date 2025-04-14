async function fetchData() {
    try {
        const response = await fetch('/data');
        const data = await response.json();
        document.getElementById('content').innerText = JSON.stringify(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
