# Regex

* [Nice basic tutorial with examples](https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-basics.php)
* [Regex refresher](http://users.cs.cf.ac.uk/Dave.Marshall/Internet/NEWS/regexp.html) — if you need a reminder of the basics, this is it.
* Regexp reference and definitions: http://www.regular-expressions.info/
* [Regexp examples](http://www.rexegg.com/)

* [Online editor](https://regexr.com/) Support PCRE

Regular expressions, while they can be utterly cryptic, entirely illegible beasts, they are also the most direct language available to programmers for writing instructions on how to process text.

Character Classes
Anchors
Escaped Characters
Groups and References
Lookaround
Quantifiers and Alternation
Substitution
Flags

## Cheatsheet

* https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-cheat-sheet.php
* https://regexr.com/

## Regexp basic concepts intro

https://stackoverflow.com/questions/4736/learning-regular-expressions

When you learn Regex, the most important part is the concepts. Once you understand how the building blocks work, differences in syntax amount to little more than mild dialects. A layer on top of your regular expression engine's syntax is the syntax of the programming language you're using.

A regular expression is a description of a pattern of characters.

Conceptually, the simplest regular expressions are literal characters. The pattern N matches the character 'N'.

Regular expressions next to each other match sequences. For example, the pattern Nick matches the sequence 'N' followed by 'i' followed by 'c' followed by 'k'.

A very basic expression like this is really no different to a search you may do in a search engine or in your favourite word processor or such.

If you've ever used grep on Unix—even if only to search for ordinary looking strings—you've already been using regular expressions! (The re in grep refers to regular expressions.)

https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-basics.php#basic

## The mechanism: how Regex are processed

The way regex works is that we have a pointer which is moved progressively through the search string. Once it comes across a character which matches the beginning of the regular expression it stops. Now a second pointer is started which moves forward from the first pointer, character by character, checking with each step if the pattern still holds or if it fails. If we get to the end of the pattern and it still holds then we have found a match. If it fails at any point then the second pointer is discarded and the main pointer continues through the string.

See here for an animated example: [Animated example](https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-basics.php#mechanism)

## Metacharacter and character class

### Intro

Adding just a little complexity, you can match either `Nick` or `nick` with the pattern `[Nn]ick`. The part in square brackets is a `character class`, which means it matches exactly one of the enclosed characters. You can also use ranges in character classes, so `[a-c]` matches either 'a' or 'b' or 'c'.

The pattern `.` is special: rather than matching a literal dot only, it matches any character. It's the same conceptually as the really big character class `[-.?+%$A-Za-z0-9...]`.

Think of character classes as menus: pick just one character from the menu; using quantifier we will see how to peek more than one.

### Character Classes

[charclass](https://www.regular-expressions.info/charclass.html)

A **character class** `[ ]`, also called "character set", matches **one character** from a set.  Simply place the characters you want to match between square brackets:

Example:  `gr[ae]y` → matches `gray` or `grey`, **not** `graay` or `graey`.

A hyphen `-` inside `[ ]` defines a **range**.  

Example:  `[0-9]` → matches any **single digit** from 0 to 9.

```bash
# NOTE: echo -e enables interpretation of backslash escapes like \n for newlines or \t for tabs
# Highlight matches for gray/grey
echo -e " gray \n grey \n graay \n graey" | grep --color=always -E 'gr[ae]y'

# Highlight any digit
echo -e " a1 \n b5 \n c10 \n dx" | grep --color=always -E '[0-9]'
```


### Negated Character Classes `[^ ]`

Placing a **caret** `^` immediately after `[` **negates** the character class.  
This makes the regex match **any character NOT listed** inside the brackets.

Example:  
- `[^0-9]` → matches any character **except** digits.  
- `[^aeiou]` → matches any character **except** vowels.


#### Important Note
A negated character class **must still match one character**.

- `q[^u]` → means "the letter `q` **followed by a character that is NOT `u`**".  
  - It **does not** mean "the letter `q` not followed by `u`".

Example:  
- In `"Iraq"`, `q[^u]` matches `q` **and the space after it** in `"Iraq is a country"`,  
  because the space counts as the "character that is not `u`".  
- It does **not** match the `q` in `"Iraq"` alone, since there is no character after `q`.

To match only the `q` **not followed by `u`**, use **negative lookahead**: `q(?!u)`.


Bash Examples (with color):

```bash
# Match any character that is NOT a digit
echo -e " a1b \n 2c3 \n xyz \n 123" | grep --color=always -E '[^0-9]'

# Match any character that is NOT a vowel
echo -e " hello \n world \n test \n apple" | grep --color=always -E '[^aeiou]'

# Match 'q' followed by any character that is NOT 'u'
echo -e " Iraq \n Iraq is a country \n quick \n queen" | grep --color=always -E 'q[^u]'
```


### Metacharacters inside a character class

https://www.regular-expressions.info/charclass.html


````markdown
### Matching Special Characters Inside Character Classes

Certain characters have **special meaning** inside `[...]` and must be **escaped** or placed carefully to match them literally.

| Character | How to match literally |
|------------|------------------------|
| `]`        | Place **first** inside the class OR escape as `\]` |
| `[`        | Escape as `\[ ` |
| `^`        | Escape as `\^` unless **first**, where it negates |
| `-`        | Escape as `\-` unless **first or last** |

---

### Example: Matching `]`, `[`, `^`, `-` After `test`

To match strings like `test]`, `test^`, `test-`, and `test[`, use:

```bash
echo -e " test] \n test^ \n test- \n test[" | grep --color=always -E 'test([]\[\\^\\-])'

# Expected Output:
# test]
# test^
# test-
# test[
````
Explanation of `([]\[\\^\\-])`:

| Pattern | Matches               |
| ------- | --------------------- |
| `[]`    | Literal `]`           |
| `\[ `   | Literal `[`           |
| `\\`    | Literal backslash `\` |
| `\^`    | Literal caret `^`     |
| `\-`    | Literal dash `-`      |

So the regex `test([]\[\\^\\-])` matches:

* `"test]"` → because `]` matches the first element
* `"test["` → because `[` matches `\[ `
* `"test^"` → because `^` matches `\^`
* `"test-"` → because `-` matches `\-`

### Repeating Character Classes

If you repeat a character class by using the `?`, `*` or `+` operators, you're repeating the entire character class. You're not repeating just the character that it matched. The regex `[0-9]+` can match 837 as well as 222.

If you want to repeat the matched character, rather than the class, you need to use backreferences. `[0-9](())\1+` matches 222 but not 837. When applied to the string 833337, it matches 3333 in the middle of this string. If you do not want that, you need to use lookaround.

```bash
# Match one or more digits (any digits, not necessarily the same)
echo -e " 123 \n 837 \n 222 \n abc" | grep --color=always -E '[0-9]+'

# Match zero or more letters
echo -e " abc \n def \n 123 \n " | grep --color=always -E '[a-z]*'

# Match optional digit
echo -e " a1 \n a \n b2 \n b" | grep --color=always -E 'a[0-9]?'
```

### Character Class Subtraction

[Reference](https://www.regular-expressions.info/charclasssubtract.html)

**Character class subtraction** matches any single character present in one list (the base class) but **not** present in another list (the subtracted class). The syntax is: `[base-[subtracted]]`

Example: to match a single letter that is **not a vowel**, you could write: `[a-z-[aeiou]]`

However, most common CLI tools like `grep`, `egrep`, `sed`, and `awk` **do not support character class subtraction**.  
Running the following command will produce an error:

```bash
echo -e "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz" \
| grep --color=always -E '[a-z-[aeiou]]'

# **Error:**
# grep: invalid character range
```

To match lowercase consonants with `grep`, you must explicitly list them:

```bash
echo -e "a\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz" \
| grep --color=always -E '[b-df-hj-np-tv-z]'
```

This matches any lowercase consonant correctly.

> [WARNING] Character class subtraction is only supported by certain regex engines like .NET and Java.
> It is **not supported** by `grep`, `sed`, `awk`, or most PCRE-based CLI tools.
> See the [reference](https://www.regular-expressions.info/charclasssubtract.html) for more details.

#### Negation and Subtraction
Negation takes precedence over subtraction. For example: `[^1234-[3456]]`

This is read as:  “**Not 1234**, then subtract 3456.”

Effectively, it matches **any character except the digits `1, 2, 3, 4, 5, 6`**.


### Character Class Intersection

[Reference](https://www.regular-expressions.info/charclassintersect.html)

**Character class intersection** matches any single character that is present in **both** character classes.  
The syntax is:`[base&&[intersection]]`

#### Example: match a consonant
To match a lowercase letter that is **not a vowel**, you can intersect the set of lowercase letters `[a-z]` with the **negation of vowels** `[^aeiou]`: `[a-z&&[^aeiou]]`

This matches any lowercase consonant.  
Without intersection, you would need to explicitly list all consonants: `[b-df-hj-np-tv-z]`

#### Example: match Thai digits
To match Thai digits, intersect the Unicode class for Thai characters `\p{IsThai}` with the Unicode class for digits `\p{Nd}`: `[\p{IsThai}&&\p{Nd}]`

This matches a single Thai digit.  
The reversed form works the same: `[\p{Nd}&&\p{IsThai}]`

#### Important note
Most CLI tools such as `grep`, `sed`, `awk`, and PCRE-based tools **do not support class intersection**.  
This feature is supported only in certain regex engines like Java and .NET.

For details and advanced examples, see the [reference](https://www.regular-expressions.info/charclassintersect.html), including:
- Intersection of multiple classes  
- Intersection inside negated classes

### Shorthand Character Classes

https://www.regular-expressions.info/shorthand.html

Since certain character classes are used often, a series of shorthand character classes are available:

* \d is short for [0-9]
* \w stands for "word character", matches the ASCII characters [A-Za-z0-9_]
* \s stands for "whitespace character", matches [ \t\r\n\f]. That is: \s matches a space, a tab, a line break, or a form feed.
* ..... TODO: add more shorthand

Shorthand character classes can be used both inside and outside the square brackets. \s\d matches a whitespace character followed by a digit. [\s\d] matches a single character that is either whitespace or a digit.

```bash
# Match any digit using \d shorthand
echo -e " abc123 \n def456 \n ghi789 \n jkl" | grep --color=always -E '\\d'

# Match word characters using \w shorthand
echo -e " hello_world \n test123 \n @#$% \n abc" | grep --color=always -E '\\w'

# Match whitespace characters using \s shorthand
echo -e " hello world \n hello\tworld \n hello\nworld \n helloworld" | grep --color=always -E '\\s'

# Match whitespace followed by digit
echo -e " a 1 \n b\t2 \n c\n3 \n d4" | grep --color=always -E '\\s\\d'

# Match single character that is either whitespace or digit
echo -e " a 1 \n b\t2 \n c\n3 \n d4" | grep --color=always -E '[\\s\\d]'
```

## The Dot Matches (Almost) Any Character

In regular expressions, the dot or period is one of the most commonly used metacharacters. Unfortunately, it is also the most commonly misused metacharacter.

The dot matches a single character, without caring what that character is. The only exception are line break characters.

This exception exists mostly because of historic reasons. The first tools that used regular expressions were line-based. They would read a file line by line, and apply the regular expression separately to each line. The effect is that with these tools, the string could never contain line breaks, so the dot could never match them.

Modern tools and languages can apply regular expressions to very large strings or even entire files, check their documentation.

```bash
# Match any character (except newline)
echo -e " abc \n def \n ghi \n jkl" | grep --color=always -E '.'

# Match any character followed by 'bc'
echo -e " abc \n xbc \n 1bc \n bc" | grep --color=always -E '.bc'

# Match 'a' followed by any character followed by 'c'
echo -e " abc \n axc \n a1c \n ac" | grep --color=always -E 'a.c'

# Match any character repeated (greedy)
echo -e " hello \n world \n test \n " | grep --color=always -E '.*'
```

## Escaping Metacharacters

https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-basics.php#escaping

## Quantifiers

You can repeat parts of your pattern with quantifiers (called also quantifiers).

Examples: https://ryanstutorials.net/regular-expressions-tutorial/regular-expressions-basics.php#multipliers

Quantifiers allow us to increase the number of times an item may occur in our regular expression.

For example, the pattern ab?c matches 'abc' or 'ac' because the ? quantifier makes the subpattern it modifies optional.

Here is the basic set of multipliers:

* * - item occurs zero or more times.
* + - item occurs one or more times.
* ? - item occurs zero or one times.
* {5} - item occurs five times.
* {3,7} - item occurs between 3 and 7 times.
* {2,} - item occurs at least 2 times (two or more time).

Putting some of these blocks together, the pattern `[Nn]()*ick` matches all of:

* ick
* Nick
* nick
* Nnick
* nNick
* nnick
* (and so on)

The first match demonstrates an important lesson: * always succeeds! Any pattern can match zero times.

> **Note:** One point to note is that regular expressions are not wildcards. The regular expression 'c*t' does not mean 'match "cat", "cot"' etc. In this case, it means 'match zero or more 'c' characters followed by a t', so it would match 't', 'ct', 'cccct' etc.

```bash
# Zero or more 'a' characters followed by 'b'
echo -e " b \n ab \n aab \n aaab \n cb" | grep --color=always -E 'a*b'

# One or more digits
echo -e " 123 \n 456 \n 7 \n abc" | grep --color=always -E '[0-9]+'

# Optional 'u' in 'color' or 'colour'
echo -e " color \n colour \n colur \n colr" | grep --color=always -E 'colou?r'

# Exactly 3 digits
echo -e " 123 \n 4567 \n 89 \n 000" | grep --color=always -E '[0-9]{3}'

# Between 2 and 4 letters
echo -e " ab \n abc \n abcd \n abcde \n a" | grep --color=always -E '[a-z]{2,4}'

# At least 2 digits
echo -e " 12 \n 123 \n 1234 \n 1" | grep --color=always -E '[0-9]{2,}'

# Zero or more 'c' followed by 't'
echo -e " t \n ct \n cct \n cccct \n cat" | grep --color=always -E 'c*t'
```

## Grouping

https://www.regular-expressions.info/brackets.html

By placing part of a regular expression inside round brackets or parentheses, you can group that part of the regular expression together. This allows you:

* to apply a quantifier to the entire group or to restrict alternation to part of the regex.
* stores the part of the string matched by the part of the regular expression inside the parentheses.

> **Note:** You can reuse the text inside the regular expression via a backreference. Backreferences can also be used in replacement strings.

A quantifier modifies the pattern to its immediate left. You might expect `0abc+0` to match `0abc0`, `0abcabc0`, and so forth, but the pattern immediately to the left of the plus quantifier is `c`. This means `0abc+0` matches `0abc0`, `0abcc0`, `0abccc0`, and so on.

To match one or more sequences of `abc` with zeros on the ends, use `0(abc)+0`.

The parentheses `()` denote a subpattern that can be quantified as a unit.

It's also common for regular expression engines to save or "capture" the portion of the input text that matches a parenthesized group. Extracting bits this way is much more flexible and less error-prone than counting indices and substr.

Example: The regex Set(Value)? matches Set or SetValue. In the first case, the first (and only) capturing group remains empty. In the second case, the first capturing group matches Value.

```bash
# Without grouping: 'c' is repeated, not 'abc'
echo -e " 0abc0 \n 0abcc0 \n 0abccc0 \n 0abcabc0" | grep --color=always -E '0abc+0'

# With grouping: entire 'abc' group is repeated
echo -e " 0abc0 \n 0abcabc0 \n 0abcabcabc0 \n 0abcc0" | grep --color=always -E '0(abc)+0'

# Optional group: 'Value' is optional
echo -e " Set \n SetValue \n SetValueValue \n SetOther" | grep --color=always -E 'Set(Value)?'

# Multiple groups with quantifiers
echo -e " hello123 \n hello123456 \n hello \n world456" | grep --color=always -E '(hello|world)[0-9]+'

# Group for alternation scope
echo -e " cat \n dog \n mouse \n fish" | grep --color=always -E '(cat|dog)'
```

### Non-Capturing Groups

Syntax: `(:?   )`

Refs:

* https://www.regular-expressions.info/brackets.html
* https://stackoverflow.com/questions/3512471/what-is-a-non-capturing-group-what-does-do

If you do not need the group to store the captured match but only to apply a quantifier, you can optimize this regular expression into `Set(?:Value)?`

Consider the following text:

```
https://stackoverflow.com/
https://stackoverflow.com/questions/tagged/regex
```

Now, if I apply the regex below over it...

`[^\r\n]((https?|ftp)://([^/\r\n]+)(/)*)?`
... I would get the following result:

Match "https://stackoverflow.com/"
     Group 1: "http"
     Group 2: "stackoverflow.com"
     Group 3: "/"

Match "https://stackoverflow.com/questions/tagged/regex"
     Group 1: "http"
     Group 2: "stackoverflow.com"
     Group 3: "/questions/tagged/regex"
But I don't care about the protocol -- I just want the host and path of the URL. So, I change the regex to include the non-capturing group (?:).

`[^\r\n]((?:https?|ftp)://([^/\r\n]+)(/)*)?`
Now, my result looks like this:

Match "https://stackoverflow.com/"
     Group 1: "stackoverflow.com"
     Group 2: "/"

Match "https://stackoverflow.com/questions/tagged/regex"
     Group 1: "stackoverflow.com"
     Group 2: "/questions/tagged/regex"
See? The first group has not been captured. The parser uses it to match the text, but ignores it later, in the final result.

## Backreferences

https://www.regular-expressions.info/backref.html

## Using Backreferences To Match The Same Text Again

Backreferences match the same text as previously matched by a capturing group. Suppose you want to match a pair of opening and closing HTML tags, and the text in between. By putting the opening tag into a backreference, we can reuse the name of the tag for the closing tag. Here's how: `[^>](<([A-Z][A-Z0-9]*)\b)*>.*?</\1>`. This regex contains only one pair of parentheses, which capture the string matched by `[A-Z0-9]([A-Z])*`. This is the opening HTML tag. (Since HTML tags are case insensitive, this regex requires case insensitive matching.) The backreference \1 (backslash one) references the first capturing group. \1 matches the exact same text that was matched by the first capturing group. The / before it is a literal character. It is simply the forward slash in the closing HTML tag that we are trying to match.

To figure out the number of a particular backreference:

* scan the regular expression from left to right. Count the opening parentheses of all the numbered capturing groups. The first parenthesis starts backreference number one, the second number two, etc.
* Skip parentheses that are part of other syntax such as non-capturing groups. This means that non-capturing parentheses have another benefit: you can insert them into a regular expression without changing the numbers assigned to the backreferences. This can be very useful when modifying a complex regular expression.

You can reuse the same backreference more than once. `[a-c](())x\1x\1` matches axaxa, bxbxb and cxcxc.

### TODO

TODO read:

* "Backtracking Into Capturing Groups" https://www.regular-expressions.info/backref.html
* https://www.regular-expressions.info/backref2.html

```bash
# Match repeated characters: same character repeated
echo -e " aa \n bb \n cc \n ab \n ba" | grep --color=always -E '([a-z])\\1'

# Match HTML tags with backreference
echo -e " <EM>text</EM> \n <B>bold</B> \n <I>italic</I> \n <EM>text</B>" | grep --color=always -E '<([A-Z][A-Z0-9]*)>.*?</\\1>'

# Match repeated pattern: axaxa, bxbxb, cxcxc
echo -e " axaxa \n bxbxb \n cxcxc \n axbxa \n axaxb" | grep --color=always -E '([a-c])x\\1x\\1'

# Match repeated words
echo -e " hello hello \n world world \n hello world \n test test" | grep --color=always -E '\\b(\\w+)\\s+\\1\\b'

# Match repeated digits
echo -e " 11 \n 22 \n 33 \n 12 \n 21" | grep --color=always -E '([0-9])\\1'
```

## Named Capturing Groups and Backreferences

https://www.regular-expressions.info/named.html

PROBLEM: Long regular expressions with lots of groups and backreferences may be hard to read. They can be particularly difficult to maintain as adding or removing a capturing group in the middle of the regex upsets the numbers of all the groups that follow the added or removed group.

SOLUTION: Python's re module was the first to offer a solution: named capturing groups and named backreferences.

`(?P<name>group)` captures the match of group into the backreference "name". name must be an alphanumeric sequence starting with a letter. group can be any regular expression. You can reference the contents of the group with the named backreference (?P=name). The question mark, P, angle brackets, and equals signs are all part of the syntax. Though the syntax for the named backreference uses parentheses, it's just a backreference that doesn't do any capturing or grouping. The HTML tags example can be written as `[^>](`<(?P<tag>[A-Z][A-Z0-9]*)\b)*>.*?</(?P=tag)>`

## Relative Backreferences

- [ ] https://www.regular-expressions.info/backrefrel.html

## Branch Reset Groups

- [ ] https://www.regular-expressions.info/branchreset.html

## Free-Spacing Regular Expressions

https://www.regular-expressions.info/freespacing.html

## Unicode

- [ ] https://www.regular-expressions.info/unicode.html

## Mode Modifiers

- [ ] https://www.regular-expressions.info/modifiers.html

## TODO

https://www.regular-expressions.info/atomic.html

* Atomic Grouping
* Possessive Quantifiers
* Lookahead & Lookbehind
* Lookaround, part 2
* Keep Text out of The Match
* Conditionals
* Balancing Groups
* Recursion
* Subroutines
* Infinite Recursion
* Recursion & Quantifiers
* Recursion & Capturing
* Recursion & Backreferences
* Recursion & Backtracking
* POSIX Bracket Expressions
* Zero-Length Matches
* Continuing Matches

## Alternation

Earlier, we saw one way to match either 'Nick' or 'nick'. Another is with alternation as in Nick|nick. Remember that alternation includes everything to its left and everything to its right. Use grouping parentheses to limit the scope of |, e.g., (Nick|nick).

For another example, you could equivalently write [a-c] as a|b|c, but this is likely to be suboptimal because many implementations assume alternatives will have lengths greater than 1.

> **Warning:** The regex engine is eager but Text-Directed Engine returns the Longest Match.

It stops searching as soon as it finds a valid match. The consequence is that in certain situations, the order of the alternatives matters. Suppose you want to use a regex to match a list of function names in a programming language: Get, GetValue, Set or SetValue. The obvious solution is Get|GetValue|Set|SetValue. Let's see how this works out when the string is SetValue.

Contrary to what we intended, the regex did not match the entire string. There are several solutions. One option is to take into account that the regex engine is eager, and change the order of the options. If we use GetValue|Get|SetValue|Set, SetValue is attempted before Set, and the engine matches the entire string.

The best option is probably to express the fact that we only want to match complete words. We do not want to match Set or SetValue if the string is SetValueFunction. So the solution is \b(Get|GetValue|Set|SetValue)\b or \b(Get(Value)?|Set(Value)?)\b. Since all options have the same end, we can optimize this further to \b(Get|Set)(Value)?\b.

Alternation is where regex-directed and text-directed engines differ. When a text-directed engine attempts Get|GetValue|Set|SetValue on SetValue. It always returns the longest match, in this case SetValue.

> **Note:** The POSIX standard leaves it up to the implementation to choose a text-directed or regex-directed engine. A BRE that includes backreferences needs to be evaluated using a regex-directed engine.

```bash
# Simple alternation: match 'cat' or 'dog'
echo -e " cat \n dog \n mouse \n fish" | grep --color=always -E 'cat|dog'

# Alternation with grouping to limit scope
echo -e " Nick \n nick \n Nnick \n nNick" | grep --color=always -E '(Nick|nick)'

# Problematic order: 'Set' matches before 'SetValue'
echo -e " SetValue \n Set \n GetValue \n Get" | grep --color=always -E 'Get|GetValue|Set|SetValue'

# Better order: longer matches first
echo -e " SetValue \n Set \n GetValue \n Get" | grep --color=always -E 'GetValue|Get|SetValue|Set'

# Word boundaries to match complete words only
echo -e " SetValue \n SetValueFunction \n Set \n GetValue" | grep --color=always -E '\\b(Get|Set)(Value)?\\b'

# Multiple alternatives
echo -e " red \n blue \n green \n yellow \n purple" | grep --color=always -E 'red|blue|green'
```

## Optional Items - Question Mark

https://www.regular-expressions.info/optional.html

The question mark makes the preceding token in the regular expression optional. colou?r matches both colour and color. The question mark is called a quantifier.

You can make several tokens optional by grouping them together using parentheses, and placing the question mark after the closing parenthesis. E.g.: Nov(ember)? matches Nov and November.

You can write a regular expression that matches many alternatives by including more than one question mark. Feb(ruary)? 23(rd)? matches February 23rd, February 23, Feb 23rd and Feb 23.

You can also use curly braces to make something optional. colou{0,1}r is the same as colou?r.

### Question Mark Greediness

The question mark is the first metacharacter introduced by this tutorial that is greedy. The question mark gives the regex engine two choices: try to match the part the question mark applies to, or do not try to match it. The engine always tries to match that part. Only if this causes the entire regular expression to fail, will the engine try ignoring the part the question mark applies to.

The effect is that if you apply the regex Feb 23(rd)? to the string Today is Feb 23rd, 2003, the match is always Feb 23rd and not Feb 23. You can make the question mark lazy (i.e. turn off the greediness) by putting a second question mark after the first.

The discussion about the other repetition operators has more details on greedy and lazy quantifiers.

```bash
# Optional 'u' in 'color' or 'colour'
echo -e " color \n colour \n colur \n colr" | grep --color=always -E 'colou?r'

# Optional group: 'ember' is optional
echo -e " Nov \n November \n NovDec \n Novem" | grep --color=always -E 'Nov(ember)?'

# Multiple optional parts: month and day suffix
echo -e " Feb 23rd \n Feb 23 \n February 23rd \n February 23" | grep --color=always -E 'Feb(ruary)? 23(rd)?'

# Using curly braces for optional (same as ?)
echo -e " color \n colour \n colur \n colr" | grep --color=always -E 'colou{0,1}r'

# Greedy vs lazy question mark
echo -e " Feb 23rd \n Feb 23 \n Feb 23rd, 2003" | grep --color=always -E 'Feb 23(rd)?'
```

## Repetition: Star, Plus operators and curly brackets

One repetition operator or quantifier was already introduced: the question mark. It tells the engine to attempt to match the preceding token zero times or once, in effect making it optional.

The asterisk or star tells the engine to attempt to match the preceding token zero or more times. The plus tells the engine to attempt to match the preceding token once or more. `[A-Za-z0-9](<[A-Za-z])*>` matches an HTML tag without any attributes. The angle brackets are literals. The first character class matches a letter. The second character class matches a letter or digit. The star repeats the second character class. Because we used the star, it's OK if the second character class matches nothing. So our regex will match a tag like <B>. When matching <HTML>, the first character class will match H.

I could also have used `[A-Za-z0-9](<)+>`. I did not, because this regex would match <1>, which is not a valid HTML tag. But this regex may be sufficient if you know the string you are searching through does not contain any such invalid tags.

### Limiting Repetition

There's an additional quantifier that allows you to specify how many times a token can be repeated. The syntax is {min,max}, where min is zero or a positive integer number indicating the minimum number of matches, and max is an integer equal to or greater than min indicating the maximum number of matches. If the comma is present but max is omitted, the maximum number of matches is infinite. So {0,1} is the same as ?, {0,} is the same as *, and {1,} is the same as +. Omitting both the comma and max tells the engine to repeat the token exactly min times.

You could use `[0-9](\b[1-9]){3}\b` to match a number between 1000 and 9999. `[0-9](\b[1-9]){2,4}\b` matches a number between 100 and 99999. Notice the use of the word boundaries.

### Watch Out for The Greediness!

Suppose you want to use a regex to match an HTML tag. You know that the input will be a valid HTML file, so the regular expression does not need to exclude any invalid use of sharp brackets. If it sits between sharp brackets, it is an HTML tag.

Most people new to regular expressions will attempt to use `<.+>`. They will be surprised when they test it on a string like This is a <EM>first</EM> test. You might expect the regex to match <EM> and when continuing after that match, </EM>.

But it does not. The regex will match *<EM>first</EM>*. Obviously not what we wanted. The reason is that the plus is greedy. That is, the plus causes the regex engine to repeat the preceding token as often as possible. Only if that causes the entire regex to fail, will the regex engine backtrack. That is, it will go back to the plus, make it give up the last iteration, and proceed with the remainder of the regex.

The dot matches E, so the regex continues to try to match the dot with the next character. M is matched, and the dot is repeated once more. The next character is the >. You should see the problem by now. The dot matches the >, and the engine continues repeating the dot. The dot will match all remaining characters in the string. The dot fails when the engine has reached the void after the end of the string. Only at this point does the regex engine continue with the next token: >.

#### Laziness Instead of Greediness

The quick fix to this problem is to make the plus lazy instead of greedy.

You can do that by putting a question mark after the plus in the regex. You can do the same with the star, the curly braces and the question mark itself. So our example becomes `<.+?>`

This tells the regex engine to repeat the dot as few times as possible. The minimum is one. So the engine matches the dot with E. The requirement has been met, and the engine continues with > and M. This fails. Again, the engine will backtrack. But this time, the backtracking will force the lazy plus to expand rather than reduce its reach. So the match of .+ is expanded to EM, and the engine tries again to continue with >. Now, > is matched successfully. The last token in the regex has been matched. The engine reports that <EM> has been successfully matched.

#### An Alternative to Laziness

In this case, there is a better option than making the plus lazy. We can use a greedy plus and a negated character class: `[^>](<)+>`. The reason why this is better is because of the backtracking. When using the lazy plus, the engine has to backtrack for each character in the HTML tag that it is trying to match. When using the negated character class, no backtracking occurs at all when the string contains valid HTML code. Backtracking slows down the regex engine.

```bash
# Zero or more letters (star)
echo -e " hello \n world \n 123 \n " | grep --color=always -E '[a-z]*'

# One or more digits (plus)
echo -e " 123 \n 456 \n 7 \n abc" | grep --color=always -E '[0-9]+'

# HTML tag matching (basic)
echo -e " <B> \n <HTML> \n <div> \n <1>" | grep --color=always -E '<[A-Za-z][A-Za-z0-9]*>'

# Limiting repetition: exactly 3 digits
echo -e " 123 \n 4567 \n 89 \n 000" | grep --color=always -E '[0-9]{3}'

# Limiting repetition: between 2 and 4 letters
echo -e " ab \n abc \n abcd \n abcde \n a" | grep --color=always -E '[a-z]{2,4}'

# Greedy matching: matches too much
echo -e " <EM>first</EM> \n <B>bold</B> \n <I>italic</I>" | grep --color=always -E '<.+>'

# Lazy matching: matches individual tags
echo -e " <EM>first</EM> \n <B>bold</B> \n <I>italic</I>" | grep --color=always -E '<.+?>'

# Better alternative: negated character class
echo -e " <EM>first</EM> \n <B>bold</B> \n <I>italic</I>" | grep --color=always -E '<[^>]+>'
```

## Escaping

Although some characters match themselves, others have special meanings. The pattern \d+ doesn't match backslash followed by lowercase D followed by a plus sign: to get that, we'd use \\d\+. A backslash removes the special meaning from the following character.

## Greediness

> **Warning:** ho fatto solo un copia incolla, andrebbe approfondito

Regular expression quantifiers are greedy. This means they match as much text as they possibly can while allowing the entire pattern to match successfully.

For example, say the input is

"Hello," she said, "How are you?"

You might expect ".+" to match only 'Hello,' and will then be surprised when you see that it matched from 'Hello' all the way through 'you?'.

To switch from greedy to what you might think of as cautious, add an extra ? to the quantifier. Now you understand how \((.+?)\), the example from your question works. It matches the sequence of a literal left-parenthesis, followed by one or more characters, and terminated by a right-parenthesis.

If your input is '(123) (456)', then the first capture will be '123'. Non-greedy quantifiers want to allow the rest of the pattern to start matching as soon as possible.

## Anchors

https://regexr.com/3p6ki

https://www.regular-expressions.info/anchors.html

Anchors can be used to "anchor" the regex match at a certain position.

The caret ^ matches the position before the first character in the string.

Example:

* Applying ^a to abc matches a.
* ^b does not match abc at all, because the b cannot be matched right after the start of the string

Similarly, $ matches right after the last character in the string.

Example:

* c$ matches c in abc
* while a$ does not match at all.

```bash
# Match 'a' at the beginning of line
echo -e " abc \n def \n aaa \n bbb" | grep --color=always -E '^a'

# Match 'c' at the end of line
echo -e " abc \n def \n ccc \n bbb" | grep --color=always -E 'c$'

# Match lines that start with 'hello'
echo -e " hello world \n world hello \n hello there \n goodbye" | grep --color=always -E '^hello'

# Match lines that end with 'world'
echo -e " hello world \n world hello \n goodbye world \n hello there" | grep --color=always -E 'world$'

# Match entire line (start to end)
echo -e " hello \n hello world \n world \n goodbye" | grep --color=always -E '^hello$'
```

## Word boundaries

https://www.regular-expressions.info/wordboundaries.html

The metacharacter `\b` is an anchor like the caret and the dollar sign. It matches at a position that is called a "word boundary". This match is zero-length.

There are three different positions that qualify as word boundaries:

* Before the first character in the string, if the first character is a word character.
* After the last character in the string, if the last character is a word character.
* Between two characters in the string, where one is a word character and the other is not a word character.

Simply put: \b allows you to perform a "whole words only" search using a regular expression in the form of \bword\b.

Example:  \b4\b can be used to match a 4 that is not part of a larger number. This regex does not match 44 sheets of a4.

```bash
# Match whole word 'cat'
echo -e " cat \n cats \n category \n bobcat \n cat" | grep --color=always -E '\\bcat\\b'

# Match whole word '4' (not part of larger number)
echo -e " 4 \n 44 \n a4 \n 4sheets \n page4" | grep --color=always -E '\\b4\\b'

# Match word boundary at start of word
echo -e " hello \n world \n hello-world \n hello_world" | grep --color=always -E '\\bhello'

# Match word boundary at end of word
echo -e " hello \n world \n hello-world \n hello_world" | grep --color=always -E 'world\\b'

# Match complete words only
echo -e " test \n testing \n contest \n test123" | grep --color=always -E '\\btest\\b'
```

## Alternation

https://www.regular-expressions.info/alternation.html

You can use alternation to match a single regular expression out of several possible regular expressions.

If you want to search for the literal text cat or dog, separate both options with a vertical bar or pipe symbol: cat|dog. If you want more options, simply expand the list: cat|dog|mouse|fish.

The alternation operator has the lowest precedence of all regex operators. That is, it tells the regex engine to match either everything to the left of the vertical bar, or everything to the right of the vertical bar. If you want to limit the reach of the alternation, you need to use parentheses for grouping. If we want to improve the first example to match whole words only, we would need to use \b(cat|dog)\b.

```bash
# Simple alternation: match 'cat' or 'dog'
echo -e " cat \n dog \n mouse \n fish" | grep --color=always -E 'cat|dog'

# Multiple alternatives
echo -e " cat \n dog \n mouse \n fish \n bird" | grep --color=always -E 'cat|dog|mouse|fish'

# Alternation with grouping to limit scope
echo -e " cat \n dog \n mouse \n fish" | grep --color=always -E '(cat|dog)'

# Whole words only with word boundaries
echo -e " cat \n cats \n category \n dog \n dogs \n dogma" | grep --color=always -E '\\b(cat|dog)\\b'

# Alternation with quantifiers
echo -e " red \n blue \n green \n yellow \n purple" | grep --color=always -E '(red|blue|green)+'
```

# Examples

http://www.rexegg.com/regex-cookbook.html

## Extract HTML comments

https://regexr.com/3p6ki
