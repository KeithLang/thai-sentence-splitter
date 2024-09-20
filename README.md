# Thai Sentence Splitter

This is a simple website using Flask and Vanilla JS to split Thai sentences into words, deployable on Vercel.

## Deploying to Vercel

Follow these steps to deploy your Thai Sentence Splitter app on Vercel:

1. Sign up for a Vercel account at https://vercel.com if you haven't already.

2. Install the Vercel CLI by running the following command in your terminal:
   ```
   npm install -g vercel
   ```

3. Open a terminal and navigate to your project directory.

4. Log in to your Vercel account using the CLI:
   ```
   vercel login
   ```

5. Deploy your app by running:
   ```
   vercel
   ```

6. Follow the prompts in the CLI:
   - Select "N" when asked if you want to link to an existing project.
   - Choose a name for your project or press Enter to use the default name.
   - Confirm that the detected Framework Preset is "Other".
   - Set the root directory to `.` (current directory).
   - Override the build command with `pip install -r requirements.txt`.
   - Change the output directory to `.` (current directory).
   - Confirm the deployment settings.

7. Wait for the deployment to complete. Vercel will provide you with a URL for your deployed app.

8. Visit the provided URL to see your Thai Sentence Splitter app live on Vercel!

## Local Development

To run the app locally:

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```
   python main.py
   ```

3. Open your browser and navigate to `http://localhost:5000` to use the app locally.

Enjoy using your Thai Sentence Splitter app!
