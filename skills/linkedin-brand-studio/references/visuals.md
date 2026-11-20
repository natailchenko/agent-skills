# Visuals

## Palette and type
Agree on 6–8 color tokens: a dark base (for cover backgrounds), a main color, a light tint, a soft tint, white, and ONE accent used once per image. Fonts: one strong display face for headlines (for example Montserrat ExtraBold) and one readable body face (for example Inter). Write them into `brand/visual-style.md`.

## Signature line
Small, bottom-left on every image: `<Name> · <short tagline>`. The tagline names what they talk about and their tone, not a job title (job titles change). Only if they want one (intake question 20). Make it theirs: build each option from words that already appear in their CV, profile or writing samples (their field, their kind of work, a phrase they use), so it could not belong to anyone else. Propose 3 options with different shapes, for example:
- a plain statement of their field and audience ("Data tools for small clinics")
- an image from their work ("Notes from the warehouse floor")
- a short promise in their own phrasing ("Teaching teams to read their numbers")

Avoid stock tone words and ready-made formulas that many people already use as taglines (honestly, unfiltered, real talk, simplified, "X, explained"). Never offer the same line to two people, and don't reuse the examples above as they are.

## Covers (1080×1350, 4:5)
Use `assets/cover-template.html`. Three types, rotate them so the feed doesn't look the same:
1. **Meme in a frame**: for light posts with humor. One meme per post, about the post's actual point. Crop out generator watermarks.
2. **Their photo in a frame + short headline**: for personal or reflective posts. Use a question to readers or their own position as the headline, never someone else's quote.
3. **Question card**: big headline only, for series like interview notes.
Headline ≤8 words with one accent word. No checklists or long text on the image: that lives in the post.

Render with headless Chrome (no extra install):
```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1080,1350 --virtual-time-budget=8000 --allow-file-access-from-files \
  --screenshot="$PWD/ready/<slug>/cover.png" "file://$PWD/brand/templates/<slug>-cover.html"
```
Open the PNG and check it before showing: wrapped words, overlaps, watermarks. Fix once, then show.

## Photos
Keep a shortlist in `brand/photos.md` with where each photo was used. Don't reuse the same photo or outfit within ~4 weeks. Crop to 4:5 with `sips -c <h> <w> --cropOffset <y> <x>`. Check photos for company logos and stickers before using.

## Memes and rights
Meme templates are other people's images. Fine for personal, non-promotional posts. Cartoons are safer than photos of real people. If a post is ever sponsored, use original images.
