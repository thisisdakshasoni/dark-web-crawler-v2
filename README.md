

<!DOCTYPE html>
<h1>Deep Web Guardian</h1>

<p><strong>Deep Web Guardian</strong> is a Python tool designed to perform various tasks related to web scraping, vulnerability scanning, link analysis, and website scanning.</p>

<h2>Features</h2>
<ul>
    <li><strong>Scrape from Single URL:</strong> Allows users to scrape a single website URL and perform link analysis.</li>
    <li><strong>Onion Link Finder:</strong> Scrapes onion links from ahmia.fi search results.</li>
    <li><strong>Vulnerability Scanning (XSS):</strong> Scans a URL for Cross-Site Scripting (XSS) vulnerabilities.</li>
    <li><strong>Extract Emails:</strong> Extracts email addresses from websites.</li>
    <li><strong>Link Analysis:</strong> Analyzes the internal and external links on a webpage.</li>
    <li><strong>Website Scanning:</strong> Scans a specified website URL for specific keywords related to vulnerabilities, security, attacks, or exploits.</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone this repository:</li>
    <pre><code>git clone &lt;repository-url&gt;</code></pre>
    <li>Install the required dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
</ol>

<h2>Usage</h2>
<ol>
    <li>Run the <code>main.py</code> file:</li>
    <pre><code>python main.py</code></pre>
    <li>Choose an option from the presented menu:</li>
    <ul>
        <li>Enter the corresponding option number to perform the desired task.</li>
        <li>Follow the prompts to input necessary information such as URLs or search queries.</li>
    </ul>
</ol>

<h2>Dependencies</h2>
<ul>
    <li>Python 3.11</li>
    <li>Requests</li>
    <li>Beautiful Soup 4</li>
    <li>dnspython</li>
</ul>

<h2>Notes</h2>
<ul>
    <li>Make sure to have Tor installed and running if using the Onion Link Finder feature.</li>
    <li>Some features may require additional setup or configuration.</li>
    <li>Use Ctrl+C to exit the program.</li>
</ul>

</body>
</html>
