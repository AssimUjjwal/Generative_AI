- Use the Resume_parser.py script to parse the resume document and convert it into a structured output file called Resume_output.txt.

- Use the GPT4_Summery.py script to query a detailed introduction for the resume using the Resume_output.txt file as input. This will generate a summary of the resume, which will be saved in a file called Resume_summary.txt.

- Use the Campaign_create.py script to create a campaign for the video resume. This script will take inputs such as the project name, the summary file (Resume_summary.txt), and the video template to be used for generating the video.

- Run the video_generate.py script to generate the video using the campaign details. This script will take inputs such as the project name and the campaign ID, and will generate the video based on the template and summary provided.

- Use the Video_status.py script to check the status of the video generation process. This script will show the progress of the video generation, including the status of each step in the process.

- Once the video has been generated, use the URL provided by the output of the video_generate.py script to fetch the video and store it for use.