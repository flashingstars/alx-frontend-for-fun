# ACCESSIBILITY

## This folder has solutions to questions covering the following topics
- ARIA's main purpose
- WCAG conformance levels(A, AA and AAA)
- Importance of Web Accessibility
- Tools to use for Web Accessibility

## The following are the questions
0. Let’s start by the “Work” section (given a sample HTML and CSS file):

We have an issue with the focus (moving from one link to another with the TAB key) in the Desktop version. With the DevTools, you can active the focus on the <a> inside .card-title and nothing happen.

To solve it, we need to update the way we are managing the hover state of .card-title:

    - In your keyboard/01-styles.css file, in the /* Card WORK section
        - Remove opacity: 0 inside .card-work .card-title
        - Remove .card-work:hover .card-inner
        - Remove .card-work:hover .card-title
        - Target the selector .card-work .card-title a and add an opacity to 0.
        - For .card-work .card-title a with the a in state focus and .card-work:hover .card-title a:
            - Property: opacity, Value: 1
            - Property: height, Value: 100%
            - Property: background-color, Value: rgba(0, 0, 0, 0.7)
Now you use the keyboard to navigate, you should see the card with the title and the dark background like when you hover the card with your mouse.

All the other elements have a blue outline around.