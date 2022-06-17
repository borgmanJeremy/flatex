# Flatex
This is inspired by the C program "flatex" for flattening a LaTex project that uses include statements. It is not a fully backwards compatible bug for bug re-implementation.

## Basic usage
The basic way to use this program is to nagivate to the directory with your highest level .tex file and simply call 

```
python <top_level.tex>
```

Then this program will output a fully expanded version

## Caveats
This will not handle nested include statements