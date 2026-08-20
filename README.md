# Wedding Invite - Modern Pakistani Wedding Invitation Generator

A modern, elegant web application for creating and sending personalized Pakistani-style wedding invitations online.

## Features

- **Wedding Creation** - Create wedding invitations with 4 beautiful Pakistani themes (Mehndi, Barat, Nikah, Walima)
- **CSV Upload** - Upload guest lists with validation and duplicate prevention
- **Unique Links** - Auto-generate personalized invitation links for each guest
- **WhatsApp Sharing** - Send invitations directly via WhatsApp with pre-filled messages
- **Admin Dashboard** - Manage weddings, guests, search, and delete functionality
- **Mobile-First** - Fully responsive design optimized for WhatsApp sharing
- **Smooth Animations** - Beautiful Framer Motion animations throughout

## Tech Stack

- **Frontend:** Next.js 16, TypeScript, Tailwind CSS, Framer Motion
- **Database:** Supabase (PostgreSQL)
- **CSV Parsing:** PapaParse
- **Deployment:** Vercel

## Prerequisites

- Node.js 18+
- npm or yarn
- A [Supabase](https://supabase.com) account

## Setup Instructions

### 1. Clone and Install

```bash
git clone <your-repo-url>
cd wedding-invite
npm install
```

### 2. Set Up Supabase

1. Create a new project at [supabase.com](https://supabase.com)
2. Go to **SQL Editor** and run the following schema:

```sql
-- Create weddings table
CREATE TABLE weddings (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID NOT NULL,
  bride_name TEXT NOT NULL,
  groom_name TEXT NOT NULL,
  event_type TEXT NOT NULL CHECK (event_type IN ('mehndi', 'barat', 'nikah', 'walima')),
  date DATE NOT NULL,
  time TIME NOT NULL,
  venue TEXT NOT NULL,
  venue_address TEXT,
  theme TEXT NOT NULL CHECK (theme IN ('mehndi', 'barat', 'nikah', 'walima')),
  message TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create guests table
CREATE TABLE guests (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  wedding_id UUID REFERENCES weddings(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  contact TEXT NOT NULL,
  unique_slug TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index for fast slug lookup
CREATE INDEX idx_guests_unique_slug ON guests(unique_slug);

-- Create index for wedding_id lookups
CREATE INDEX idx_guests_wedding_id ON guests(wedding_id);

-- Enable Row Level Security (optional but recommended)
ALTER TABLE weddings ENABLE ROW LEVEL SECURITY;
ALTER TABLE guests ENABLE ROW LEVEL SECURITY;

-- Allow public read access to guests (for invitation pages)
CREATE POLICY "Public can view guests" ON guests
  FOR SELECT USING (true);

-- Allow public insert to guests (for CSV upload)
CREATE POLICY "Allow guest inserts" ON guests
  FOR INSERT WITH CHECK (true);

-- Allow public delete from guests (for admin)
CREATE POLICY "Allow guest deletes" ON guests
  FOR DELETE USING (true);

-- Allow public read access to weddings (for invitation pages)
CREATE POLICY "Public can view weddings" ON weddings
  FOR SELECT USING (true);

-- Allow public insert to weddings (for creation)
CREATE POLICY "Allow wedding inserts" ON weddings
  FOR INSERT WITH CHECK (true);
```

3. Copy your **Project URL** and **Anon Key** from Settings > API

### 3. Configure Environment Variables

```bash
cp .env.example .env.local
```

Edit `.env.local`:

```env
NEXT_PUBLIC_SUPABASE_URL=your-project-url-here
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
```

### 4. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

## CSV File Format

The CSV file should have exactly two columns:

```csv
name,contact
Muhammad Riaz,+923001234567
Farzana Perveen,+923111234567
Saad Riaz,+923221234567
```

## Deployment to Vercel

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and import your repository
3. Add environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
4. Deploy!

## Project Structure

```
src/
├── app/
│   ├── layout.tsx          # Root layout with fonts
│   ├── page.tsx            # Landing page
│   ├── globals.css         # Global styles
│   ├── create/
│   │   └── page.tsx        # Wedding creation form
│   ├── dashboard/
│   │   └── page.tsx        # Admin dashboard
│   └── invite/
│       └── [slug]/
│           └── page.tsx    # Personalized invitation page
├── lib/
│   ├── supabase.ts         # Supabase client
│   └── themes.ts           # Theme definitions & utilities
└── types/
    └── index.ts            # TypeScript types
```

## Themes

| Theme | Description |
|-------|-------------|
| **Mehndi** | Elegant green with floral patterns and gold details |
| **Barat** | Deep maroon with luxury gold typography |
| **Nikah** | Ivory and white with minimal elegance |
| **Walima** | Pastel white with modern luxury design |

## License

Made with love for beautiful celebrations.
