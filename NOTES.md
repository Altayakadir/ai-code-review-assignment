# Notes

### Question 1

I considered using a pandas DataFrame for numpy-backed parallelized computation, but this really only makes sense when the data is huge. Considering the fact that most cases won't require that much speed, I decided to stick with my current solution.

I noticed the original code didn't try to convert strings to floats—it just crashed if you gave it one. Because of that, I decided to treat string inputs as 'invalid data' and filter them out entirely. I figured it's safer to skip ambiguous strings than to force a conversion and risk messing up the total.
### Question 2

My first thought was to use Regex. However, a proper email regex is really complex and makes the code hard to read. I decided to use the industry-standard library instead to keep the solution clean and readable.

### Question 3

If we knew that all the input data was convertible to float, we could solve this faster using a list comprehension. However, since the float conversion had to be handled inside a try-except block, I could not use a list comprehension.