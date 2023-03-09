# CMPUT404Project

**The 5 members of the group are as follows:**
1. Javin Vora (jvora)
2. Avnish Jadhav (jadhav)
3. Saakshi Joshi (saakshi)
4. Zhiyuan Yu (zyu6)
5. Lok Him Isaac Cheng (lokhimis)

**The links that were used/referred to while completing the work for the part 1 are as follows:**
1. We referred to this link: https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM in order to understand how to document the test cases for our project.
2. We referred to this some of videos in order to understand Django application and funtionalities from the follwing link: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
3. We also referred a set of videos from the following link: https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi in order to inspire us on implementing certain features.

**API Documentation**
These are the API for the Part 1.
***Users
    - URL: ://api/users/{AUTHOR_ID}/
      - Allow: GET, POST, HEAD, OPTIONS
    - Example Format:
      #+BEGIN_SRC json
      {
        "url": "http://localhost:8000/api/users/1/",
        "username": "admin",
        "email": "admin@domain.com"
      }
      #+END_SRC