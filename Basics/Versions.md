# Python 2 vs Python 3

## Main differences

<ul>
    <li><strong>print</strong>: it is used as a keyword in Python 2, but the recommended way is as a function (using parentheses).</li>

    <li><strong>strings</strong>: default adoption of Unicode (UTF). It was before ASCII.</li>

    <li><strong>Integer division</strong>: the division between integers now returns a float.</li>

    <li><strong>Handling exceptions</strong>: in Python 3 we have to use the "as" keyword now.</li>

    <li><strong>Input vs raw_input</strong>: the input() function was fixed in Python 3 so that it always stores the user inputs as str objects. In order to avoid the dangerous behavior in Python 2 to read in other types than strings, we have to use raw_input() instead.</li>
</ul>

> More information: https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html