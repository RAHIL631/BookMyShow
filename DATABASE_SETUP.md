# Database Setup for Vercel

The "unable to open database file" error occurs because Vercel is a serverless environment and does not support SQLite for persistent storage. To fix this, you need to use a PostgreSQL database.

## 1. Create a Free Database
Go to [Neon.tech](https://neon.tech/) or [Supabase](https://supabase.com/) and create a free PostgreSQL project.

## 2. Get your Connection String
Copy the connection string (DATABASE_URL). It should look like this:
`postgres://user:password@hostname:port/dbname`

## 3. Add to Vercel
1. Go to your **Vercel Dashboard** -> **Project Settings** -> **Environment Variables**.
2. Add a new variable:
   - **Key**: `DATABASE_URL`
   - **Value**: `[Your Connection String]`
3. Add your `SECRET_KEY` and set `DEBUG` to `False` as well.

## 4. Redeploy
Once the variables are added, go to the **Deployments** tab and select **Redeploy** for the latest commit. The app will now connect to your persistent database.
