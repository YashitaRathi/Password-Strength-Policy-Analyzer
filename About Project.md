# **Password strength analyzer**

* ask input from user
* analyze the password

> at least 12 characters long or 9 character long - done

> should include a combination of letters (both uppercase and lowercase), numbers, and characters. - done

> password shouldn’t contain any consecutive letters or numbers (i.e. ABCD, 1234, etc.)

> password shouldn’t be the word “password” or the same letter or number repeated.

* give result if its a strong password or not
* Password Policy Analyzer: audit an organization's password requirements against industry standard like missed guidelines. Company has weak password and don't realize it. The tool evaluate their requirements, suggest improvements and explains why each change matters using references to actual breach statistics.

This show that I understand compliance, it is a security tool, and can communicate security concepts to non technical stakeholders

### Process -

1\. Wrote the basic code to ask password from user and then show the input also added points.

2\. Wrote code to analyze the password if it contains upper and lower character, at least 9 digits, special characters.

3\. If it contains more than 5 points strong password and if not then medium and weaker character.

4\. It was all happening in terminal so I decided to code some GUI program to make it visible in window.

5\. Found tkinter - a built in library in python to create desktop GUI apps

6\. Made a basic UI using tkinter.

7\. I saw a video explaining how I can make this password strength analyzer a better thing for my project resume so I start to do some changes

8\. First I add three files names - main.py, password\_checker.py, policy\_analyzer.py

9\. Wrote NIST(National Institute of Standards and Technology ) password guideline of 2025 which is:

a. Use longer passwords(minimum 8 and maximum 64)

b. Drop complexity requirements(accept all types of characters, including spaces, and encourage unique and memorable phrases, also known as passphrases.)

c. No more forced password resets(resetting password every few months is considered bad practice which results in weaker password security.)

d. Maintain a password blocklist(Stop easy-to-exploit passwords at source and use checking services to ensure that people don’t use compromised passwords that have been exposed in breaches)

e. Eliminate security questions and hints(Knowledge-based questions are too susceptible to social engineering (What was your first pet?). Instead, rely on more-secure recovery methods)

f. Use modern security tools(Limit the number of failed login attempts, require multi-factor authentication (MFA), and use tools like enterprise password managers)

10\. Now the next question for me to solve was "How do I represent NIST rules in code so I can compare them with an organization’s policy?" and I thought of using dictionary, why because - I need to show numbers, boolean and recommendations and it should be in a clean code and NIST rule has a name, a value, a description, an explanation and "*dictionary is perfect for key value mapping*"

11\. Now next process is to give NIST rules a name for dicitionary - min\_length, password\_requirement, password\_expiration, password\_blocklist, no\_security\_question, login\_attempts, mfa\_applied

12\. Writing code for the nested dictionary - expected, description, explanation

13\. Working on GUI

14\.





Kivy is an open-source, cross-platform Python framework for building GUI applications. It supports Windows, macOS, Linux, Android and iOS and is optimized for natural user interfaces (NUI), including multi-touch and gesture-based interactions.

Kivy follows “write once, run everywhere” principle, allowing Python applications to run on multiple platforms without changing the code.

Developed a desktop-based security auditing tool using Python and Kivy. Implemented modular analysis logic, NIST-compliant policy evaluation, and a GUI for non-technical users.





import kivy
from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget

from kivy.uix.checkbox import CheckBox

from kivy.graphics import Rectangle, Color





and at the end "A().run()"



### Kivy Tools:

#### \- Widget:

1. ##### Label Widget :display text on the screen eg: Label(text='Hello Kivy') font\_size='24sp': increases the label text size (use sp for scalable units). color=(r,g,b,a): RGBA tuple with values from 0 to 1; here it makes the text bluish. The Label is centered by default in a bare app window. multiple lines of text, you can use newline characters (\\n). text\_size=(300, None) gives the label a fixed wrapping width so halign can center lines. halign='center' centers text horizontally; valign='middle' centers vertically within the text\_size area. Markup allows you to style parts of the text within a label using BBCode-like tags. You can make text bold, colored, italic, underlined and more, without using multiple label widgets. text='\[b]Bold\[/b] and \[color=ff3333]Red\[/color] text', markup=True, markup=True tells Kivy to parse BBCode-like tags. \[b]...\[/b] makes text bold; \[color=RRGGBB]...\[/color] sets text color (hex).
2. ##### TextInput Widget: A TextInput is a widget in Kivy that provides an editable text box on the screen. It allows users to enter single-line or multi-line text, supports cursor movement, text selection, clipboard operations and can trigger events like pressing Enter. TextInput(text='', multiline=True, password=False, hint\_text(placeholder shown when text is empty)=None, font\_size=None, size\_hint(control widget sizing in layouts.)=(1,1))
3. ##### Canvas: A Canvas in Kivy is a container used for drawing shapes, colors, and images on a widget. Each widget has its own canvas by default and you can add instructions like Rectangle, Color, or Line to display custom graphics. with widget.canvas: Color(r, g, b, a) Rectangle(pos=(x, y), size=(w, h), source='image.jpg'). pos: position of the shape, relative to the window or widget. size: width and height of the shape. source: optional; image file to display inside the rectangle. Color(r, g, b, a): sets the color (0–1 values for red, green, blue, alpha). Bind pos and size if you want shapes to adjust when the widget changes.
4. ##### Checkbox: A CheckBox is a two-state button in Kivy that can be checked or unchecked. It is used along with a Label to indicate whether a setting is active. Checkboxes can also trigger events when their state changes. CheckBox(pos = (105,140) active=False,). You can attach a callback using bind(active=callback) to detect state changes.
5. ##### Dropdown List:
6. ##### Slider:
7. ##### Switch:
8. ##### Spinner:
9. ##### Progress Bar:
10. ##### ScrollView:
11. ##### Carousel



- Buttons
- Layout
- KV Design Language































Does your tool work?

Does it show you understand security principles?

Did you follow standards (NIST 800-63B)?

Did you design modular, clean logic?

Can you explain your reasoning?

Do you know how to build software end-to-end?



| Check Type | Example Weakness | What You Add to “Reasons” |

| ------------------- | ---------------- | ------------------------------------------------------ |

| Blocklist | “password” | “Password is too common and appears in breach lists.” |

| Repetitive | “aaaaaa” | “Password contains repeated characters.” |

| Numeric sequence | “12345678” | “Password contains predictable numeric sequence.” |

| Alphabetic sequence | “abcdefg” | “Password contains predictable alphabetical sequence.” |

| Keyboard patterns | “qwerty” | “Password contains keyboard patterns.” |

| Common construction | “hello123” | “Password uses a common word + number pattern.” |

