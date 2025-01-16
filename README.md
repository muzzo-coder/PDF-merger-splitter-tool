<hr>

<h2>Application Title: PDF Merger and Splitter Tool</h2>

<hr>

<h3>1. Overview</h3>
<p>This Python application is designed to:</p>
<ul>
    <li>Merge multiple PDF files into a single document.</li>
    <li>Split a single PDF file into individual pages.</li>
</ul>
<p>It provides a simple, user-friendly interface for handling PDF files efficiently and ensures compatibility across different systems.</p>

<hr>

<h3>2. Features</h3>
<ul>
    <li><strong>Merge PDFs</strong>: Combine multiple PDF files into one consolidated document.</li>
    <li><strong>Split PDFs</strong>: Split a single PDF into separate files for each page.</li>
    <li><strong>Error Handling</strong>: Detects and handles errors such as invalid file paths or unsupported formats.</li>
    <li><strong>Logging</strong>: Keeps track of operations and errors in a log file for troubleshooting.</li>
</ul>

<hr>

<h3>3. Prerequisites</h3>
<p>Ensure you have the following installed on your system:</p>
<ul>
    <li><strong>Python 3.7 or higher</strong></li>
    <li>Required Python libraries: <code>PyPDF2</code></li>
</ul>
<p>To install the library, use:</p>
<pre><code>pip install PyPDF2</code></pre>

<hr>

<h3>4. How to Run the Application</h3>
<ol>
    <li>Download or clone the application files from the repository.</li>
    <li>Open a terminal or command prompt in the application directory.</li>
    <li>Run the script:</li>
    <pre><code>python pdf_tool.py</code></pre>
    <li>Follow the prompts to either merge or split PDFs.</li>
</ol>

<hr>

<h3>5. Usage</h3>
<h4>5.1 Merge PDFs</h4>
<ol>
    <li>Choose the "Merge PDFs" option in the menu.</li>
    <li>Enter the paths of the PDF files you want to merge, separated by commas (e.g., <code>file1.pdf, file2.pdf</code>).</li>
    <li>Specify the output file name (e.g., <code>merged.pdf</code>).</li>
    <li>The application will create a merged PDF in the specified location.</li>
</ol>

<h4>5.2 Split a PDF</h4>
<ol>
    <li>Choose the "Split PDF" option in the menu.</li>
    <li>Enter the path of the PDF file you want to split.</li>
    <li>Specify the folder where the split pages will be saved.</li>
    <li>The application will generate individual files for each page of the PDF.</li>
</ol>

<hr>

<h3>6. Application Structure</h3>
<h4>6.1 Files</h4>
<ul>
    <li><code>pdf_tool.py</code>: Main Python script for running the application.</li>
    <li><code>log.txt</code>: Optional file for logging application operations and errors.</li>
</ul>

<h4>6.2 Functions</h4>
<ul>
    <li><strong>merge_pdfs(file_list, output_file)</strong>: Merges the list of PDF files into a single output file.</li>
    <li><strong>split_pdf(input_file, output_dir)</strong>: Splits a single PDF file into individual pages saved in the specified directory.</li>
</ul>

<hr>

<h3>7. Error Handling</h3>
<p>The application includes robust error handling for:</p>
<ul>
    <li>Invalid file paths or missing files.</li>
    <li>Incorrect file formats.</li>
    <li>Permission issues for reading or writing files.</li>
</ul>

<hr>

<h3>8. Additional Notes</h3>
<ul>
    <li>Ensure the input PDF files are not password-protected.</li>
    <li>Use absolute file paths for better reliability.</li>
    <li>Logs for operations can be found in <code>log.txt</code>.</li>
</ul>

<hr>

<h3>9. Contact Information</h3>
<p>For support or further queries, contact:</p>
<ul>
    <li><strong>Name</strong>: Mujjamil Sofi</li>
    <li><strong>Email</strong>: [your-email@example.com]</li>
</ul>

<hr>

<p>This documentation ensures the application is easy to set up and use, even for users with minimal technical knowledge.</p>
