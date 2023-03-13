def body_name(name,kind):
    body=None
    if kind=="first":
        body = f"""\
    <html>
      <head>
        <style>
          /* Define styles for email body */
          body {{
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.5;
            color: #333;
            padding: 20px;
            background-color: #f4f4f4;
          }}
          h1 {{
            font-size: 24px;
            color: #0070c0;
            margin-top: 0;
            margin-bottom: 20px;
          }}
          p {{
            margin-bottom: 20px;
          }}
          a {{
            color: #0070c0;
            text-decoration: none;
            border-bottom: 1px solid #0070c0;
          }}
          strong {{
            font-weight: bold;
            color: #0070c0;
          }}
          .highlight {{
            background-color: #e9f5ff;
            padding: 5px 10px;
            border-radius: 5px;
          }}
          .signature {{
            margin-top: 30px;
            border-top: 1px solid #ccc;
            padding-top: 20px;
            color: #555;
          }}
          .logo {{
            display: block;
            margin: 0 auto;
            width: 150px;
            height: 150px;
            background-image: url('https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/v1397195895/0f0170cb4061db03f605f2a1841982c7.jpg');
            background-size: cover;
          }}
        </style>
      </head>
      <body>
        <div class="logo"></div>
        <h1>Exciting Python Programming Opportunity at hushHush Company</h1>
        <p><strong>Dear candidate,</strong></p>
        <p>We have an exciting offer for you related to your ability in <strong>Python programming</strong> at <strong>hushHush Company</strong>. We are excited to learn more about your skills and qualifications for the role.</p>
        <p>As part of our recruitment process, we require all candidates that we narrow it down using <strong>Machine Learning</strong> to complete a coding challenge to demonstrate their technical abilities.</p>
        <p>The challenge can be accessed through the attached file.</p>
        <p>The challenge consists of solving a mathematical problem that needs to be solved within two weeks.</p>
        <p>You can use <strong>Python programming language</strong> to solve the problem. Once you have completed the challenge, please reply to this email and attached your code with the name like <strong style="background-color: red">{name}.py</strong>.</p>
        <p>After implementing your solution, you can easily <strong>modify the attached file </strong>and send it back to us.</p> 
        <p>We understand that completing a coding challenge can be time-consuming, but it is an important part of our recruitment process as we want to ensure that we are hiring the most qualified and capable candidates for the position.</p>
        <p>If you have any questions or concerns about the coding challenge, please do not hesitate to <a href="mailto:shahriyarbabaki@gmail.com">reach out to us</a>. We are happy to provide any clarification or assistance you may need.</p>
        <p>Thank you again for your interest in joining our team. We look forward to reviewing your coding challenge submission and learning more about your technical skills and abilities.</p>
        <div class="signature">
          <p>Best regards,</p>
          <p>The Recruitment Team</p>
          <p>hushHush Company</p>
        </div>
      </body>
    </html>
    """
    elif kind=="failed":
        body=f'''
        <html>
            <head>
                <style>
                    /* Add any desired styling here */
                    body {{
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: auto;
                        padding: 20px;
                        border: 1px solid #ccc;
                        border-radius: 10px;
                    }}
                    .logo {{
                        text-align: center;
                    }}
                    .logo img {{
                        width: 200px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="logo">
                        <img src="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/v1397195895/0f0170cb4061db03f605f2a1841982c7.jpg" alt="Company Logo">
                    </div>
                    <p>Dear Applicant,</p>
                    <p>Thank you for your interest in the position at our company and taking the time to interview with us. We appreciate the opportunity to learn more about your qualifications and experience.</p>
                    <p>After careful consideration, we have decided not to move forward with your application at this time. We received many strong applications and while we were impressed with your qualifications, we have decided to pursue other candidates who more closely match our current needs.</p>
                    <p>We appreciate your interest in our company and thank you again for your time and effort throughout the application and interview process. We wish you all the best in your future endeavors.</p>
                    <p>Sincerely,</p>
                    <p>Recruitment Team</p>
                </div>
            </body>
        </html>
        '''





    elif kind=="confirmed":
        body=f"""
    <div style="background-color: #66bb6a; padding: 20px;">
        <img src='https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/v1397195895/0f0170cb4061db03f605f2a1841982c7.jpg' alt="Company Logo" style="width: 200px;" />
        <h1 style="color: white;">Job Offer</h1>
        <p style="color: white;">
            Dear {name},
        </p>
        <p style="color: white;">
            Congratulations! We are delighted to inform you that you have passed our evaluation process
            and we would like to offer you the position of programmer at hushHush.
        </p>
        <p style="color: white;">
            We were impressed with your skills, experience, and performance in the evaluation process,
            and we believe you would be a great addition to our team.
        </p>
        <p style="color: white;">
            The details of the position and the compensation package will be discussed in more
            detail during your orientation. If you accept the offer, please reply to this email with
            your acceptance and let us know when you would be available to start.
        </p>
        <p style="color: white;">
            Once again, congratulations on your successful evaluation and we look forward to working
            with you.
        </p>
        <p style="color: white;">Sincerely,</p>
        <p style="color: white;"> Recruitment Team from hushHush</p>
    </div>
"""
    return body
