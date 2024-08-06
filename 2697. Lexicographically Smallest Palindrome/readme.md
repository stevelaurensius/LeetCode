# [2697. Lexicographically Smallest Palindrome](https://leetcode.com/problems/lexicographically-smallest-palindrome)

## Description
<p>Your laptop keyboard is faulty, and whenever you type a character <code>'i'</code> on it, it reverses the string that you have written. Typing other characters works as expected.</p>

<p>You are given a <strong>0-indexed</strong> string <code>s</code>, and you type each character of <code>s</code> using your faulty keyboard.</p>

<p>Return <em>the final string that will be present on your laptop screen.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "string"
<strong>Output:</strong> "rtsng"
<strong>Explanation:</strong> 
After typing first character, the text on the screen is "s".
After the second character, the text is "st". 
After the third character, the text is "str".
Since the fourth character is an 'i', the text gets reversed and becomes "rts".
After the fifth character, the text is "rtsn". 
After the sixth character, the text is "rtsng". 
Therefore, we return "rtsng".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "poiinter"
<strong>Output:</strong> "ponter"
<strong>Explanation:</strong> 
After the first character, the text on the screen is "p".
After the second character, the text is "po". 
Since the third character you type is an 'i', the text gets reversed and becomes "op". 
Since the fourth character you type is an 'i', the text gets reversed and becomes "po".
After the fifth character, the text is "pon".
After the sixth character, the text is "pont". 
After the seventh character, the text is "ponte". 
After the eighth character, the text is "ponter". 
Therefore, we return "ponter".</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>s[0] != 'i'</code></li>
</ul><div class="elfjS" data-track-load="description_content"><p>You are given a string <code node="[object Object]">s</code> consisting of <strong>lowercase English letters</strong>, and you are allowed to perform operations on it. In one operation, you can <strong>replace</strong> a character in <code node="[object Object]">s</code> with another lowercase English letter.</p>

<p>Your task is to make <code node="[object Object]">s</code> a <strong>palindrome</strong> with the <strong>minimum</strong> <strong>number</strong> <strong>of operations</strong> possible. If there are <strong>multiple palindromes</strong> that can be <meta charset="utf-8">made using the <strong>minimum</strong> number of operations, <meta charset="utf-8">make the <strong>lexicographically smallest</strong> one.</p>

<p>A string <code>a</code> is lexicographically smaller than a string <code>b</code> (of the same length) if in the first position where <code>a</code> and <code>b</code> differ, string <code>a</code> has a letter that appears earlier in the alphabet than the corresponding letter in <code>b</code>.</p>

<p>Return <em>the resulting palindrome string.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "egcfe"
<strong>Output:</strong> "efcfe"
<strong>Explanation:</strong> The minimum number of operations to make "egcfe" a palindrome is 1, and the lexicographically smallest palindrome string we can get by modifying one character is "efcfe", by changing 'g'.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> "abba"
<strong>Explanation:</strong> The minimum number of operations to make "abcd" a palindrome is 2, and the lexicographically smallest palindrome string we can get by modifying two characters is "abba".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "seven"
<strong>Output:</strong> "neven"
<strong>Explanation:</strong> The minimum number of operations to make "seven" a palindrome is 1, and the lexicographically smallest palindrome string we can get by modifying one character is "neven".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code>&nbsp;consists of only lowercase English letters<b>.</b></li>
</ul>
</div>