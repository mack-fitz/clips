# Golf accounts analysis — Oct 5–20, 2026 (raw tables)

Pulled from Zernio analytics_get_analytics on Oct 20 (~01:30 MT sync), one page per account (all results fit). Joined to repo metadata (mackygolfs-mackthegolfer state/trials.json, review_archive_2026-10-19.json, posted_index.json; clips state/inventory.json) by Zernio id / latePostId / platformPostUrl. Times are Mountain. `young` = under ~30 h old at sync (left out of best/worst and group stats). `follows` is null for every post (Zernio/IG doesn't return it), so follows per 1k views can't be computed. @moremackygolfs: 'emotionally that was a par' (Oct 12) is excluded as bought (state/schedule.json inflated: 1,142 views / 100 likes on reach 127).

Labels: kind = native (Mack posted it herself) / new (our pipeline, never-posted footage) / reedit (pipeline, footage already on IG) / comp / shorty. trial = not shared to feed (isSharedToFeed false). gap = days since the same footage was last on @mackygolfs or @mackthegolfer. Opening/cover known only for pipeline posts (A = shirt-wipe open by rule, B = talk-first). `content` for native posts is inferred from caption/source only.

## Top-line per account (Oct 5–20)

| account | posts | total views | median | mean | likes | comments | shares | saves | followers Oct 13 → 20 |
|---|---|---|---|---|---|---|---|---|---|
| @mackygolfs IG | 34 | 424,877 | 8,264 | 12,496 | 6,039 | 451 | 519 | 1,414 | 29,797 → 30,069 (+272) |
| @mackthegolfer IG | 42 | 624,247 | 4,704 | 14,863 | 6,158 | 550 | 688 | 724 | 6,703 → 7,012 (+309) |
| @moremackygolfs IG (excl. bought post) | 19 (Oct 11–19) | 23,351 | 578 | 1,229 | 208 | 13 | 33 | 20 | 299 now; 442 were bought, so real growth can't be separated |
| @mackygolfs TikTok | 25 (Oct 11–19) | 414,852 | 6,537 | 16,594 | 11,490 | 389 | 307 | 1,128 | 283 (Oct 12) → 2,486 (+2,203) |
| @mackygolfs X | 21 (Oct 12–18) | 499 | 22 | 24 | 21 | 4 | 0 | 0 | 2 → 18 |
| macky.golfs Facebook | 13 (Oct 15–19) | 19,531 | 258 | 1,502 | 11 | 6 | 0 | 0 | 0 → 2 |

Split by week (IG): @mackygolfs median Oct 5–11 = 15,541 (n=16) vs Oct 12–20 = 3,584 (n=18). @mackthegolfer Oct 5–11 = 12,773 (n=17) vs Oct 12–20 = 3,803 (n=25). Oct 12–20 split by who posted: A native 15,267 median (n=4) vs pipeline 2,933 (n=12); B native 785 (n=4) vs pipeline 4,347 (n=18).

Context outliers (before the window): @mackthegolfer Sep 30 'what do you thinking I'm shooting??' 1,069,793 views; @mackygolfs Sep 29 'all children were safe (this time)' 721,223. Inside the window: B Oct 5 'do you think the singing is helping or hurting my game' 285,394 and A Oct 15 'let me know what you need instructions on next' 68,061 — medians are used for that reason.

## @mackygolfs per post (Oct 5–20, newest first)

| date MT | views | reach | likes | cmts | shares | saves | AWT s | skip % | dur s | watch % | trial | kind | open | cover | gap d | content / trip | caption |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10-19 18:51 (young) | 1,790 | 1,299 | 15 | 0 | 2 | 1 | 13.0 | 33.1 | 25 | 52 | Y | new | wipe | wipe+text |  | guess-score (par 4, bunker) / CO red Hawaiian | what do you think I’m shooting on this par 4? |
| 10-19 17:48 (young) | 3,089 | 2,022 | 29 | 4 | 1 | 17 | 6.9 | 31 | 8 | 86 | Y | native | unk | unk |  | short bit / ? | really tough think to reckon with |
| 10-18 18:49 | 149 | 129 | 1 | 0 | 0 | 0 | 12.5 | 42.2 | 135 | 9 | Y | reedit | wipe | wipe+text | 7 | guess-score (par 3) / TX green | lock in your guess before i tee off. no cheating |
| 10-18 07:39 | 3,964 | 2,925 | 76 | 9 | 0 | 6 | 9.4 | 44 | 24 | 39 |  | reedit | wipe | wipe+text | 11 | bad hole / self-deprecating / light blue print | let’s just assume bogey is normal for me |
| 10-17 18:47 | 10,291 | 7,815 | 210 | 13 | 9 | 36 | 13.5 | 39 | 29 | 47 |  | new | wipe | wipe+text |  | par 5 + hot dog / CO red Hawaiian | did someone say hot dogs |
| 10-17 13:20 | 21,831 | 15,149 | 447 | 29 | 9 | 77 | 9.7 | 27 | 15 | 65 |  | native | unk | unk |  | short bit / ? | just goonin 🦀 |
| 10-16 18:46 | 8,014 | 6,228 | 196 | 19 | 2 | 10 | 27.9 | 44.4 | 148 | 19 |  | new | wipe | wipe |  | rate-me full hole / TX Amarillo | six months of golf. rate me |
| 10-16 07:39 | 178 | 153 | 2 | 0 | 0 | 2 | 6.1 | 51.6 | 35 | 18 | Y | reedit | wipe | wipe+text | 4 | near hole-in-one par 3 / TX green | called the hole in one. got the par |
| 10-15 23:03 | 68,061 | 50,595 | 456 | 6 | 189 | 406 | 15.2 | 20.7 | 32 | 48 | Y | native | unk | unk |  | fake lesson / instructional bit / ? | let me know what you need instructions on next 🙏 |
| 10-15 18:54 | 6,647 | 5,413 | 165 | 37 | 1 | 6 | 17.6 | 57.3 | 111 | 16 |  | new | wipe | wipe+text |  | guess-score full par 3 / TX Amarillo | guess my score pls |
| 10-15 07:44 | 170 | 141 | 0 | 0 | 0 | 0 | 7.1 | 51.4 | 175 | 4 | Y | new | wipe | wipe+text |  | cactus / blow-up par 5 / TX San Angelo | fr are they poisonous |
| 10-14 18:47 | 172 | 141 | 2 | 0 | 0 | 0 | 9.3 | 47.5 | 51 | 18 | Y | reedit | wipe | wipe+text | 7 | drives / Bomb City / TX Amarillo | before you say this isn’t a bomb watch my other drives |
| 10-14 14:19 | 8,703 | 7,400 | 237 | 18 | 7 | 23 | 21.9 | 52.8 | 172 | 13 |  | native | unk | unk |  | full hole (triple dipper) / TX green polo | You me par four? 👉👈 |
| 10-14 11:38 | 6,110 | 5,273 | 92 | 10 | 3 | 20 | 6.0 | 61 | 30 | 20 |  | native | unk | unk |  | short bit / ? | top 4 |
| 10-13 18:41 | 2,660 | 2,021 | 30 | 4 | 5 | 7 | 10.9 | 39.5 | 25 | 44 | Y | new | wipe | wipe |  | rate-me par 3 / CO black shirt sunset | par 3 at sunset. rate it |
| 10-13 12:35 | 1,419 | 1,216 | 13 | 0 | 2 | 7 | 7.4 | 28.1 | 22 | 34 | Y | comp | wipe | wipe |  | shirt-wipe montage / mixed | sorry I'm so wet |
| 10-12 18:52 | 5,577 | 4,891 | 119 | 13 | 3 | 7 | 16.5 | 65.2 | 169 | 10 |  | new | wipe | wipe |  | full hole (double) / TX San Angelo | no disrespect to the san angels |
| 10-12 09:01 | 3,205 | 2,535 | 32 | 4 | 7 | 11 | 12.9 | 31.7 | 48 | 27 | Y | reedit | wipe | plain | 1 | blow-up par 4 (11 on a par 4) / rain day | long journey to break 100 |
| 10-11 18:56 | 9,087 | 7,520 | 152 | 29 | 0 | 11 | 9.8 | 51.1 | 44 | 22 |  | native | unk | unk |  | ? / ? | should I have just googled this |
| 10-11 17:07 | 5,825 | 4,946 | 106 | 28 | 5 | 7 | 20.7 | 63.8 | 153 | 14 |  | native | unk | unk |  | guess-score full hole / TX green | I will take offense if you guess high based on the looks of me btw |
| 10-11 14:10 | 23,492 | 13,630 | 738 | 53 | 20 | 208 | 7.9 | 37.3 | 7 | 112 |  | native | unk | unk |  | short bit / ? | have you ever been bored |
| 10-11 13:08 | 15,579 | 12,284 | 273 | 9 | 15 | 42 | 14.9 | 40.9 | 66 | 23 |  | native | unk | unk |  | funny swing / CO orange checker | new swing just dropped |
| 10-11 08:56 | 19,557 | 15,613 | 251 | 13 | 18 | 79 | 11.0 | 42.8 | 48 | 23 |  | native | unk | unk |  | blow-up hole / rain day | absolutely brutal |
| 10-10 16:02 | 16,671 | 12,216 | 247 | 29 | 5 | 18 | 6.7 | 45.1 | 15 | 45 |  | native | unk | unk |  | short bit / ? | Hey |
| 10-10 08:17 | 9,585 | 7,948 | 201 | 27 | 3 | 15 | 14.8 | 51.7 | 110 | 13 |  | native | unk | unk |  | bad shot / ? | dang hate to see the ball go exactly where I was aimed :/ |
| 10-09 17:20 | 19,791 | 14,533 | 271 | 14 | 17 | 61 | 5.4 | 50.1 | 11 | 49 |  | native | unk | unk |  | short bit / ? | should I have left this in the drafts y/n |
| 10-09 14:50 | 2,923 | 2,170 | 34 | 4 | 7 | 10 | 11.4 | 36.8 |  |  | Y | native | unk | unk |  | swing help / ? | what am I doing wrong |
| 10-09 08:25 | 15,503 | 12,763 | 208 | 10 | 2 | 31 | 17.6 | 50.9 | 133 | 13 |  | native | unk | unk |  | ? / ? | if you catch me Lymed up you know why |
| 10-08 14:02 | 8,515 | 6,745 | 111 | 1 | 32 | 22 | 12.6 | 49.6 | 49 | 26 |  | native | unk | unk |  | talking bit (pick-up line) / ? | stay til the end for an elite pick up line |
| 10-07 21:44 | 24,512 | 20,365 | 262 | 20 | 14 | 50 | 11.9 | 41 | 43 | 28 |  | native | unk | unk |  | ? / ? | Ehhhh give me 6 months |
| 10-07 07:51 | 2,766 | 2,178 | 42 | 3 | 0 | 7 | 16.1 | 35.5 | 30 | 54 | Y | native | unk | unk |  | guess-score / light blue print | and please remember to consider that I am a really good golfer when lo |
| 10-06 07:15 | 54,645 | 47,297 | 571 | 20 | 71 | 151 | 13.5 | 37.3 | 53 | 25 |  | native | unk | unk |  | ? / ? | got that DAWG in me |
| 10-05 20:37 | 14,194 | 11,721 | 192 | 12 | 29 | 31 | 8.5 | 47.2 | 32 | 26 |  | native | unk | unk |  | bad hole / ? | really fell apart near the green |
| 10-05 08:17 | 30,202 | 27,088 | 258 | 13 | 41 | 35 | 6.8 | 64.2 | 52 | 13 |  | native | unk | unk |  | ? / ? | not sure what the takeaway here is |

## @mackthegolfer per post (Oct 5–20, newest first)

| date MT | views | reach | likes | cmts | shares | saves | AWT s | skip % | dur s | watch % | trial | kind | open | cover | gap d | content / trip | caption |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10-19 18:24 (young) | 1,312 | 1,118 | 13 | 0 | 0 | 0 | 28.7 | 25.7 | 46 | 62 | Y | native | unk | unk |  | ? / ? | I hate this sport actually |
| 10-19 08:26 (young) | 641 | 548 | 7 | 0 | 0 | 0 | 6.3 | 49.1 | 22 | 29 | Y | comp | talk | unk |  | asmr comp / TX San Angelo | very peaceful sport |
| 10-18 19:32 (young) | 3,803 | 2,792 | 94 | 2 | 2 | 0 | 9.6 | 35.1 | 19 | 51 |  | new | talk | plain+text |  | par 3 over pond / CO red Hawaiian | let’s take a sec for that tee shot |
| 10-18 13:48 | 2,658 | 1,791 | 16 | 1 | 0 | 1 | 10.3 | 27.9 | 14 | 74 | Y | shorty | talk | unk |  | bad drive bit / ? | not my worst |
| 10-18 08:25 | 150 | 129 | 0 | 0 | 0 | 0 | 15.3 | 40.6 | 122 | 13 | Y | reedit | talk | plain | 4 | triple-dipper hole / TX green polo | I want my baby back |
| 10-17 19:34 | 3,815 | 3,010 | 55 | 3 | 1 | 1 | 10.8 | 40.4 | 30 | 36 |  | comp | talk | unk |  | self-hype lines / mixed | being a good golfer is all about mindset mindset |
| 10-17 08:28 | 1,948 | 1,573 | 22 | 5 | 3 | 0 | 28.8 | 25.7 | 78 | 37 | Y | reedit | talk | wipe+text | 7 | Lucy Goosey par 5 / TX green polo | they call me Goosey, Lucy Goosey |
| 10-16 19:30 | 151 | 118 | 0 | 0 | 0 | 0 | 8.1 | 39 | 20 | 40 | Y | reedit | talk | plain | 3 | sunset par 3 over water / CO black shirt sunset | wet or dry?? |
| 10-16 11:29 | 263 | 154 | 1 | 0 | 0 | 0 | 9.3 | 52.9 | 11 | 84 | Y | native | unk | unk |  | short bit / ? | I cant |
| 10-16 10:52 | 3,893 | 2,994 | 52 | 5 | 2 | 6 | 27.2 | 26.9 | 88 | 31 | Y | native | unk | unk |  | ? / ? | I’m getting sooo much better!!! |
| 10-16 08:21 | 4,362 | 3,216 | 171 | 11 | 1 | 3 | 19.8 | 33.7 | 67 | 30 |  | reedit | talk | plain | 28 | worst-hole par 5 blow-up / golfclips | never seen something go so downhill so fast |
| 10-15 19:38 | 8,759 | 6,671 | 253 | 17 | 5 | 7 | 16.9 | 29.6 |  |  |  | reedit | talk | plain | 12 | perfect drive then bogey / CO orange checker | don’t be a pssy |
| 10-15 16:42 | 4,332 | 3,591 | 90 | 8 | 4 | 1 | 8.9 | 48.3 | 29 | 31 |  | comp | talk | unk |  | self-hype ("that's not bad") / mixed | i'm my biggest fan |
| 10-15 08:28 | 5,203 | 3,684 | 62 | 4 | 0 | 1 | 6.0 | 50.3 | 10 | 60 |  | shorty | talk | unk |  | reading a putt bit / light blue print | it was a 2 footer |
| 10-14 20:34 | 757 | 683 | 8 | 0 | 0 | 0 | 3.7 | 57.7 |  |  | Y | native | unk | unk |  | ? / ? | take as old as time |
| 10-14 19:17 | 5,674 | 4,422 | 171 | 4 | 2 | 1 | 18.4 | 39.2 | 81 | 23 |  | reedit | talk | plain | 6 | lag putting par 4 / TX Amarillo | and that is why she’s blue boys |
| 10-14 16:08 | 6,230 | 4,635 | 101 | 5 | 1 | 2 | 10.1 | 49.5 | 15 | 68 |  | shorty | talk | unk |  | bad drive / cart path bit / TX Amarillo | the green was right there |
| 10-14 15:37 | 4,571 | 3,787 | 71 | 0 | 1 | 3 | 6.7 | 58.8 | 22 | 31 |  | comp | talk | unk |  | excuses / mixed | it's out of my control |
| 10-14 08:23 | 5,044 | 3,929 | 138 | 7 | 1 | 2 | 9.6 | 29.9 | 25 | 38 |  | reedit | talk | plain | 7 | guess-score par 5 / light blue print | what do you think i'm shooting on this par 5 (be nice) |
| 10-13 20:29 | 813 | 687 | 2 | 0 | 0 | 0 | 9.8 | 43.2 | 38 | 26 | Y | native | unk | unk |  | good shot / mixed | but then you hit one pure 🥵🥵🥵 |
| 10-13 19:07 | 5,743 | 4,545 | 64 | 42 | 0 | 0 | 11.1 | 44.4 | 32 | 35 |  | reedit | talk | plain | 7 | breaking 100 / tips / bandana | trying to break 100. tips welcome |
| 10-13 12:39 | 4,836 | 4,010 | 122 | 4 | 0 | 0 | 8.0 | 57.1 | 38 | 21 |  | comp | talk | unk |  | angry bits / mixed | crazy this is what I do for fun |
| 10-13 08:29 | 146 | 130 | 0 | 0 | 0 | 0 | 7.3 | 56.2 | 68 | 11 | Y | reedit | teaser | plain | 7 | beach par 4 / golfclips beach | and I’m sorry to that kid |
| 10-12 14:06 | 2,176 | 1,744 | 45 | 2 | 1 | 0 | 31.2 | 30.6 | 99 | 31 | Y | new | teaser | plain |  | near hole-in-one par 3 / TX green | said hole in one. close enough |
| 10-12 09:02 | 3,701 | 3,010 | 115 | 35 | 0 | 0 | 21.7 | 57.5 | 154 | 14 |  | reedit | teaser | plain | 1 | guess-score par 3 / TX green | lock it IN this is a RIDE boys |
| 10-11 17:38 | 5,029 | 4,173 | 95 | 28 | 1 | 3 | 20.7 | 47.5 | 139 | 15 |  | native | unk | unk |  | full hole (lag master) / TX Amarillo | does anyone know the lag masta’s schedule actually |
| 10-11 10:17 | 8,428 | 6,600 | 159 | 10 | 3 | 3 | 12.7 | 39.9 | 36 | 35 |  | native | unk | unk |  | good hole / CO orange checker | one of my better holes ngl |
| 10-11 07:45 | 9,354 | 7,306 | 275 | 30 | 1 | 4 | 18.8 | 43.8 | 83 | 23 |  | native | unk | unk |  | guess-score / golfclips | don’t let the cover photo influence your guess listen to your gut |
| 10-11 07:44 | 7,835 | 5,877 | 179 | 11 | 0 | 2 | 10.3 | 44.4 | 27 | 38 |  | native | unk | unk |  | ? / ? | I think I’m getting better guys |
| 10-10 09:41 | 9,799 | 7,963 | 218 | 25 | 2 | 2 | 24.5 | 37.9 | 175 | 14 | Y | native | unk | unk |  | Lucy Goosey par 5 / TX green polo | They call me Goosey, Lucy Goosey #LGB #neverforget |
| 10-10 09:29 | 3,132 | 2,613 | 33 | 7 | 0 | 4 | 25.6 | 32.1 | 177 | 14 | Y | native | unk | unk |  | Lucy Goosey par 5 / TX green polo | LGB LOOSEY GOOSEY BABY #neverforget |
| 10-08 17:48 | 3,313 | 2,634 | 56 | 9 | 3 | 5 | 24.9 | 27.5 | 95 | 26 | Y | native | unk | unk |  | lag putting / TX Amarillo | that’s why she’s blue boys |
| 10-08 07:49 | 13,313 | 10,041 | 150 | 8 | 3 | 3 | 11.9 | 35.2 | 45 | 26 |  | native | unk | unk |  | lag putting bit / ? | INTRODUCING: The Lag Masta |
| 10-07 14:30 | 13,407 | 12,295 | 248 | 19 | 1 | 5 | 15.5 | 46.8 | 74 | 21 |  | native | unk | unk |  | drives / Bomb City / TX Amarillo | Bomb City, TX Population: @mackthegolfer |
| 10-07 07:46 | 13,595 | 12,303 | 145 | 8 | 2 | 7 | 7.7 | 55.4 | 43 | 18 |  | native | unk | unk |  | ? / ? | at least I can go to sleep |
| 10-06 19:14 | 12,773 | 10,966 | 180 | 9 | 1 | 26 | 14.8 | 23.1 | 44 | 34 | Y | native | unk | unk |  | ? / ? | I have other skills than golf btw |
| 10-06 12:45 | 14,386 | 12,501 | 231 | 9 | 6 | 7 | 12.3 | 47.6 | 97 | 13 |  | native | unk | unk |  | beach par 4 / golfclips beach | no kids were harmed this time 🙌 |
| 10-06 07:28 | 3,614 | 2,704 | 68 | 32 | 9 | 4 | 16.2 | 31.3 | 36 | 45 | Y | native | unk | unk |  | swing help / bandana | help pls 🙏 |
| 10-06 07:26 | 18,421 | 15,471 | 256 | 33 | 4 | 6 | 15.8 | 51 | 175 | 9 |  | native | unk | unk |  | wet or dry par 3 / ? | it’s not even wet or dry????? |
| 10-05 17:07 | 48,901 | 40,242 | 412 | 22 | 10 | 22 | 13.3 | 32.2 | 52 | 26 |  | native | unk | unk |  | ? / ? | I’m not wasting $32 |
| 10-05 08:11 | 72,572 | 58,092 | 231 | 5 | 14 | 8 | 9.0 | 37.9 | 30 | 30 |  | native | unk | unk |  | chipping / ? | I’ll either get better at chipping or get drunk trying |
| 10-05 07:33 | 285,394 | 213,612 | 1549 | 130 | 604 | 585 | 27.8 | 27.7 | 165 | 17 | Y | native | unk | unk |  | singing while golfing / ? | do you think the singing is helping or hurting my game |

## Group tables (A+B, excludes young posts; per-1k and AWT/skip are medians)

### Format

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| comp | 5 | 4,332 | 3,795 | 0.3 | 0.3 | 0.8 | 8.0 | 48 | 0 |
| native | 41 | 12,773 | 22,599 | 1.3 | 0.4 | 1.1 | 12.7 | 43 | 1 |
| new | 7 | 5,577 | 5,076 | 1.2 | 0.5 | 1.5 | 16.5 | 44 | 1 |
| reedit | 15 | 3,205 | 2,890 | 0.0 | 0.0 | 1.2 | 12.5 | 41 | 6 |
| shorty | 3 | 5,203 | 4,697 | 0.3 | 0.0 | 0.8 | 10.1 | 50 | 0 |

Format — @mackygolfs only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| comp | 1 | 1,419 | 1,419 | 4.9 | 1.4 | 0.0 | 7.4 | 28 | 0 |
| native | 20 | 15,541 | 18,878 | 2.6 | 0.9 | 1.0 | 11.7 | 46 | 0 |
| new | 6 | 6,112 | 5,560 | 1.3 | 0.4 | 1.9 | 15.0 | 48 | 1 |
| reedit | 5 | 178 | 1,534 | 1.5 | 0.0 | 0.0 | 9.4 | 44 | 3 |

Format — @mackthegolfer only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| comp | 4 | 4,452 | 4,388 | 0.2 | 0.2 | 0.8 | 8.4 | 53 | 0 |
| native | 21 | 9,354 | 26,142 | 0.4 | 0.2 | 1.2 | 14.8 | 40 | 1 |
| new | 1 | 2,176 | 2,176 | 0.0 | 0.5 | 0.9 | 31.2 | 31 | 0 |
| reedit | 10 | 4,032 | 3,568 | 0.0 | 0.1 | 1.7 | 16.1 | 39 | 3 |
| shorty | 3 | 5,203 | 4,697 | 0.3 | 0.0 | 0.8 | 10.1 | 50 | 0 |

### Length

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| 16-35s | 17 | 4,571 | 12,571 | 1.5 | 0.2 | 1.1 | 9.4 | 40 | 2 |
| 36-60s | 16 | 10,930 | 16,010 | 1.1 | 0.3 | 0.6 | 11.9 | 42 | 1 |
| 61-120s | 13 | 5,674 | 6,959 | 0.5 | 0.4 | 1.4 | 18.4 | 41 | 1 |
| <=15s | 8 | 11,450 | 12,017 | 0.7 | 0.2 | 0.8 | 8.6 | 47 | 1 |
| >120s | 14 | 5,701 | 26,398 | 0.9 | 0.2 | 2.2 | 20.7 | 49 | 3 |
| unknown | 3 | 2,923 | 4,146 | 0.8 | 0.6 | 1.4 | 11.4 | 37 | 0 |

Length — @mackygolfs only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| 16-35s | 9 | 3,964 | 12,183 | 3.3 | 0.9 | 1.1 | 9.4 | 40 | 1 |
| 36-60s | 8 | 14,322 | 18,737 | 2.3 | 1.1 | 0.5 | 11.5 | 45 | 1 |
| 61-120s | 3 | 9,585 | 10,604 | 1.6 | 0.3 | 2.8 | 14.9 | 52 | 0 |
| <=15s | 4 | 20,811 | 20,446 | 3.3 | 0.6 | 1.5 | 7.3 | 41 | 0 |
| >120s | 7 | 5,825 | 6,277 | 1.2 | 0.2 | 2.1 | 17.6 | 51 | 2 |
| unknown | 1 | 2,923 | 2,923 | 3.4 | 2.4 | 1.4 | 11.4 | 37 | 0 |

Length — @mackthegolfer only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| 16-35s | 8 | 4,808 | 13,008 | 0.2 | 0.2 | 1.1 | 9.3 | 42 | 1 |
| 36-60s | 8 | 10,600 | 13,284 | 0.4 | 0.2 | 0.7 | 12.3 | 38 | 0 |
| 61-120s | 10 | 4,128 | 5,866 | 0.4 | 0.4 | 1.4 | 19.3 | 36 | 1 |
| <=15s | 4 | 3,930 | 3,588 | 0.3 | 0.0 | 0.6 | 9.7 | 50 | 1 |
| >120s | 7 | 5,029 | 46,518 | 0.3 | 0.2 | 2.2 | 21.7 | 41 | 1 |
| unknown | 2 | 4,758 | 4,758 | 0.4 | 0.3 | 1.0 | 10.3 | 44 | 0 |

### Time of day

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| evening (17+) | 24 | 5,784 | 11,280 | 1.1 | 0.3 | 0.8 | 12.9 | 43 | 3 |
| midday (12-17) | 16 | 7,372 | 9,483 | 0.9 | 0.4 | 0.9 | 10.2 | 46 | 0 |
| morning (<12) | 31 | 5,203 | 19,873 | 0.5 | 0.2 | 1.2 | 12.9 | 43 | 5 |

Time of day — @mackygolfs only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| evening (17+) | 13 | 8,014 | 13,460 | 1.3 | 0.6 | 1.3 | 12.5 | 47 | 2 |
| midday (12-17) | 8 | 12,141 | 12,392 | 3.1 | 0.9 | 1.3 | 10.5 | 39 | 0 |
| morning (<12) | 11 | 6,110 | 13,262 | 2.5 | 0.3 | 0.7 | 11.0 | 51 | 2 |

Time of day — @mackthegolfer only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| evening (17+) | 11 | 5,029 | 8,703 | 0.3 | 0.2 | 0.7 | 13.3 | 39 | 1 |
| midday (12-17) | 8 | 4,704 | 6,574 | 0.3 | 0.2 | 0.8 | 10.2 | 48 | 0 |
| morning (<12) | 20 | 5,124 | 23,508 | 0.3 | 0.2 | 1.3 | 15.5 | 39 | 3 |

### Caption has engagement bait (guess/score/rate/lock/help/wet or dry/be nice…)

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| False | 56 | 6,170 | 11,807 | 0.7 | 0.3 | 0.8 | 11.6 | 43 | 6 |
| True | 15 | 5,743 | 25,152 | 0.9 | 0.2 | 1.8 | 16.1 | 44 | 2 |

Caption has engagement bait (guess/score/rate/lock/help/wet or dry/be nice…) — @mackygolfs only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| False | 25 | 9,585 | 14,966 | 2.6 | 0.8 | 0.8 | 11.0 | 45 | 3 |
| True | 7 | 5,825 | 6,550 | 1.2 | 0.2 | 1.5 | 16.1 | 44 | 1 |

Caption has engagement bait (guess/score/rate/lock/help/wet or dry/be nice…) — @mackthegolfer only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| False | 31 | 4,836 | 9,260 | 0.3 | 0.2 | 0.8 | 12.3 | 40 | 3 |
| True | 8 | 5,394 | 41,428 | 0.4 | 0.2 | 2.5 | 16.0 | 41 | 1 |

### Trial (not shared to feed)

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| False | 45 | 8,759 | 13,907 | 0.8 | 0.3 | 1.3 | 11.9 | 47 | 0 |
| True | 26 | 2,417 | 15,872 | 0.7 | 0.0 | 0.4 | 12.7 | 36 | 8 |

Trial (not shared to feed) — @mackygolfs only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| False | 22 | 12,242 | 15,377 | 2.1 | 0.7 | 1.5 | 12.3 | 48 | 0 |
| True | 10 | 2,040 | 8,170 | 3.0 | 0.7 | 0.0 | 11.1 | 38 | 4 |

Trial (not shared to feed) — @mackthegolfer only

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| False | 23 | 6,230 | 12,500 | 0.3 | 0.2 | 1.2 | 11.9 | 44 | 0 |
| True | 16 | 2,417 | 20,686 | 0.1 | 0.0 | 0.6 | 15.7 | 32 | 4 |

### Opening (pipeline new + re-edits only; A always wipe, B talk-first/teaser — confounded with account)

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| wipe | 11 | 3,205 | 3,730 | 1.3 | 0.2 | 1.3 | 12.5 | 44 | 4 |
| talk | 8 | 4,703 | 3,979 | 0.1 | 0.2 | 1.7 | 16.1 | 36 | 2 |
| teaser | 3 | 2,176 | 2,008 | 0.0 | 0.0 | 0.9 | 21.7 | 56 | 1 |

### @mackygolfs pipeline cover (new + re-edits)

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| wipe+text | 7 | 178 | 3,082 | 0.9 | 0.0 | 0.0 | 9.4 | 48 | 4 |
| wipe | 3 | 5,577 | 5,417 | 1.3 | 0.5 | 2.3 | 16.5 | 44 | 0 |
| plain | 1 | 3,205 | 3,205 | 3.4 | 2.2 | 1.2 | 12.9 | 32 | 0 |

New originals only: text covers 6,647 / 10,291 / 170 (+1,790 young); no-text covers 8,014 / 5,577 / 2,660. No usable difference.

### Re-edit spacing (pipeline re-edits/clean edits of footage already on A/B)

| group | n | median views | mean | saves/1k | shares/1k | comments/1k | AWT s | skip % | stalled (<300) |
|---|---|---|---|---|---|---|---|---|---|
| same footage on A/B within 7 days | 12 | 1,063 | 2,188 | 0.0 | 0.0 | 0.4 | 11.8 | 41 | 6 |
| 8+ days since last A/B version | 3 | 4,362 | 5,695 | 0.8 | 0.2 | 2.3 | 16.9 | 34 | 0 |
| brand-new footage (pipeline) | 7 | 5,577 | 5,076 | 1.2 | 0.5 | 1.5 | 16.5 | 44 | 1 |
| comps + shorties | 8 | 4,452 | 4,133 | 0.3 | 0.2 | 0.8 | 8.4 | 49 | 0 |

Spearman correlation with views (A+B, n≈70): saves/1k 0.38, shares/1k 0.32, caption length 0.11, avg watch time 0.07, duration −0.01, skip rate −0.03, watch % 0.00.

## Same footage across accounts

| footage | @mackygolfs | @mackthegolfer | @moremackygolfs | TikTok | X / FB |
|---|---|---|---|---|---|
| Sep 21 red Hawaiian par 5 + hot dog | 10,291 (new, Oct 17) |  |  | 107,132 (Oct 19) | FB scheduled Oct 21 |
| San Angelo cactus par 5 (7 30 44) | 170 (new, 175 s, Oct 15 am) |  |  | 9,597 |  |
| Amarillo lock-it-in par 3 (7 17 58) | 6,647 (new, 112 s) |  |  | 7,441 |  |
| Triple-dipper par 4, green polo (12 17 30) | 8,703 (Mack, 172 s) | 150 (re-edit, 4 d later) | 186 | 6,053 |  |
| Bomb City drives (7 19 40) | 172 (re-edit, 7 d after B) | 13,407 (Mack, Oct 7) | 3,867 | 11,210 |  |
| Lucy Goosey par 5 (12 22 39) |  | 9,799 + 3,132 (Mack, Oct 10); 1,948 (re-edit Oct 17); 641 asmr comp |  | 6,947 |  |
| Orange checker par 3 (9 02 57 (2)) | 15,579 (Mack) | 8,428 (Mack) | 379 | 5,344 |  |
| Rain day blow-up (12 00 30) | 19,557 (Mack Oct 11); 3,205 (pipeline next day) |  |  | 3,595 | X 25 |
| Sunset par 3 over water (7 35 57) | 2,660 (new, Oct 13) | 151 (re-edit, 3 d later) |  |  | FB 2,749 |
| Lag-putt par 4 (7 13 58) |  | 3,313 (Mack Oct 8); 5,674 (re-edit Oct 14) | 206 | 3,710 |  |
| Guess-my-score par 3 (12 05 56) | 5,825 (Mack Oct 11); 149 (re-edit Oct 18) | 3,701 (clean edit Oct 12) |  |  | FB 1,083 |
| Hole-in-one-loading par 3 (12 14 03) | 178 (re-edit, 4 d after B) | 2,176 (Oct 12) |  |  |  |
| Beach par 4 (golfclips 2CC073A6) |  | 14,386 (Mack Oct 6); 146 (re-edit Oct 13) |  |  |  |
| Light blue print putt (7 33 50) | 2,766 (Mack Oct 7); 3,964 (re-edit Oct 18) | 5,044 (clean edit Oct 14) |  |  |  |

## @moremackygolfs per post

| date MT | views | reach | likes | cmts | shares | saves | AWT s | skip % / completion | caption |
|---|---|---|---|---|---|---|---|---|---|
| 10-19 09:07 | 1,857 | 1,321 | 13 | 0 | 1 | 0 | 7.9 | 22.6 | it worked though |
| 10-18 17:43 | 186 | 169 | 1 | 0 | 0 | 0 | 10.0 | 44 | the triple dipper got me |
| 10-18 09:14 | 206 | 172 | 1 | 0 | 0 | 1 | 10.9 | 44 | tween the legs was the safe play |
| 10-17 17:55 | 280 | 223 | 4 | 0 | 13 | 1 | 17.7 | 23.3 | is there a cart path rule or not |
| 10-17 09:07 | 3,867 | 2,803 | 33 | 1 | 3 | 0 | 27.5 | 18.9 | perfect drive. then the rest of the hole happened |
| 10-16 18:31 | 319 | 260 | 0 | 0 | 0 | 0 | 9.7 | 32.8 | great drive tho |
| 10-16 11:39 | 2,653 | 1,937 | 31 | 0 | 2 | 2 | 24.2 | 25.3 | very well deserved triple |
| 10-16 09:14 | 379 | 330 | 3 | 0 | 1 | 0 | 12.5 | 24.1 | at least the shirt is nice |
| 10-15 17:47 | 325 | 275 | 3 | 1 | 0 | 0 | 8.6 | 44.6 | eagle was right there guys |
| 10-15 12:09 | 2,649 | 2,011 | 21 | 3 | 2 | 3 | 27.2 | 24.5 | pls help me |
| 10-15 08:53 | 2,442 | 1,789 | 33 | 4 | 1 | 2 | 23.9 | 25.8 | par is a myth |
| 10-14 18:24 | 1,697 | 1,365 | 12 | 0 | 0 | 1 | 19.9 | 24 | who put those rocks there |
| 10-14 12:42 | 578 | 440 | 4 | 0 | 0 | 1 | 6.6 | 40.3 | be honest. but nice |
| 10-14 09:23 | 2,957 | 1,980 | 32 | 2 | 8 | 4 | 16.6 | 27.4 | basically a hole in one |
| 10-13 11:49 | 579 | 439 | 1 | 0 | 0 | 1 | 17.2 | 39.8 | the ball is cursed not me |
| 10-13 08:41 | 423 | 350 | 1 | 0 | 0 | 2 | 8.2 | 41.9 | king of the world for 1 second |
| 10-12 19:00 | 1,320 | 284 | 100 | 0 | 0 | 0 | 13.1 | 23.1 | emotionally that was a par (EXCLUDED: bought) |
| 10-12 12:19 | 264 | 233 | 1 | 2 | 0 | 1 | 10.8 | 52.7 | guess wrong and we're enemies |
| 10-11 20:33 | 1,471 | 1,242 | 9 | 0 | 2 | 1 | 12.3 | 47.1 | 6 is basically par |
| 10-11 19:48 | 219 | 158 | 5 | 0 | 0 | 0 | 15.5 | 34.4 | golf is so easy guys |

## TikTok @mackygolfs per post

| date MT | views | reach | likes | cmts | shares | saves | AWT s | skip % / completion | caption |
|---|---|---|---|---|---|---|---|---|---|
| 10-19 18:23 | 6,947 | 0 | 273 | 10 | 1 | 25 | 15.1 | 0.033 | the marshal gave me a lesson. i lost count after that |
| 10-19 15:42 | 107,132 | 0 | 3222 | 69 | 184 | 434 | 9.0 | 0.118 | bunker, then a hot dog. if you say that's not a par we can't be friend |
| 10-19 12:23 | 7,441 | 0 | 247 | 19 | 2 | 14 | 11.1 | 0.038 | if you guessed higher than a 4 we can't be friends |
| 10-19 08:53 | 9,597 | 0 | 354 | 23 | 6 | 19 | 12.4 | 0.025 | please help. a cactus attacked me and i still have to finish this par  |
| 10-18 17:42 | 6,053 | 340 | 98 | 5 | 0 | 6 | 8.2 | 0.016 | the triple dipper got me |
| 10-18 12:15 | 4,891 | 936 | 108 | 10 | 0 | 6 | 5.0 | 0.064 | what do you call a pent-bogey |
| 10-18 08:48 | 3,595 | 572 | 66 | 8 | 3 | 3 | 4.8 | 0.024 | we don't talk about this par 4 |
| 10-17 17:54 | 5,021 | 1,493 | 166 | 13 | 2 | 9 | 10.2 | 0.028 | is there a cart path rule or not |
| 10-17 12:20 | 3,710 | 1,087 | 78 | 7 | 3 | 6 | 5.6 | 0.019 | tween the legs was the safe play |
| 10-17 09:06 | 11,210 | 6,476 | 508 | 21 | 4 | 31 | 15.4 | 0.072 | perfect drive. then the rest of the hole happened |
| 10-16 18:30 | 14,314 | 9,245 | 524 | 23 | 7 | 26 | 10.8 | 0.091 | great drive tho |
| 10-16 11:39 | 3,831 | 2,056 | 107 | 2 | 3 | 9 | 7.4 | 0.029 | very well deserved triple |
| 10-16 09:14 | 5,344 | 3,171 | 219 | 11 | 3 | 7 | 13.0 | 0.081 | at least the shirt is nice |
| 10-15 17:47 | 9,261 | 6,064 | 354 | 17 | 3 | 24 | 10.8 | 0.135 | eagle was right there guys |
| 10-15 12:08 | 4,274 | 2,664 | 142 | 7 | 4 | 2 | 7.5 | 0.036 | pls help me |
| 10-15 08:52 | 38,817 | 21,920 | 849 | 27 | 10 | 60 | 14.0 | 0.108 | par is a myth |
| 10-14 18:24 | 6,956 | 4,976 | 277 | 14 | 3 | 14 | 15.4 | 0.071 | who put those rocks there |
| 10-14 12:42 | 6,257 | 4,208 | 120 | 6 | 3 | 20 | 4.7 | 0.087 | be honest. but nice |
| 10-14 09:23 | 12,039 | 8,999 | 273 | 9 | 4 | 31 | 10.6 | 0.142 | basically a hole in one |
| 10-13 11:48 | 11,714 | 7,599 | 263 | 10 | 3 | 13 | 7.1 | 0.033 | the ball is cursed not me |
| 10-13 08:40 | 112,585 | 68,167 | 2847 | 62 | 52 | 343 | 10.4 | 0.106 | king of the world for 1 second |
| 10-12 18:04 | 6,537 | 5,437 | 94 | 1 | 7 | 9 | 5.5 | 0.025 | emotionally that was a par |
| 10-12 12:18 | 5,720 | 4,644 | 98 | 5 | 0 | 8 | 6.6 | 0.023 | guess wrong and we're enemies |
| 10-11 20:33 | 5,182 | 4,157 | 58 | 4 | 0 | 2 | 4.4 | 0.013 | 6 is basically par |
| 10-11 20:08 | 6,424 | 5,319 | 145 | 6 | 0 | 7 | 8.2 | 0.058 | golf is so easy guys |

## Facebook macky.golfs per post

| date MT | views | reach | likes | cmts | shares | saves | AWT s | skip % / completion | caption |
|---|---|---|---|---|---|---|---|---|---|
| 10-19 08:18 | 6 | 5 | 0 | 0 | 0 | 0 | 15.1 |  | par is a myth. prove me wrong #golf |
| 10-18 19:20 | 1,083 | 967 | 1 | 0 | 0 | 0 | 8.2 |  | i'm my biggest fan |
| 10-18 12:41 | 11 | 7 | 0 | 0 | 0 | 0 | 11.7 |  | this ball is cursed. not me |
| 10-18 08:27 | 12 | 11 | 0 | 0 | 0 | 0 | 3.3 |  | par 4. guess how many |
| 10-17 18:58 | 258 | 239 | 0 | 0 | 0 | 0 | 6.0 |  | why do i like this sport |
| 10-17 11:54 | 6,193 | 4,603 | 2 | 6 | 0 | 0 | 12.9 |  | guess my score. be nice |
| 10-17 08:40 | 77 | 65 | 0 | 0 | 0 | 0 | 9.3 |  | always going for the hero shot |
| 10-16 19:42 | 6,531 | 4,893 | 3 | 0 | 0 | 0 | 8.2 |  | the green was right there |
| 10-16 12:45 | 2,749 | 2,195 | 3 | 0 | 0 | 0 | 10.0 |  | par 3 at sunset. rate it |
| 10-16 07:55 | 163 | 131 | 0 | 0 | 0 | 0 | 5.5 |  | what do you call a pent-bogey? #golf |
| 10-15 19:09 | 1,229 | 1,058 | 1 | 0 | 0 | 0 | 5.6 |  | it's out of my control |
| 10-15 12:28 | 1,103 | 958 | 1 | 0 | 0 | 0 | 6.9 |  | the bandana was doing a lot of the work |
| 10-15 08:14 | 116 | 102 | 0 | 0 | 0 | 0 | 8.3 |  | hi i'm mack. really good golfer btw |
| 10-14 22:08 | 0 | 6 | 0 | 0 | 0 | 0 | 0.0 |  |  |
| 10-14 21:56 | 0 | 6 | 0 | 0 | 0 | 0 | 0.0 |  |  |

## X @mackygolfs per post

21 posts Oct 12–18, views 6–62 (median 22), 0–2 likes each, 0 shares/saves. Best: 'king of the world for 1 second' 62 views, 35 link clicks; 'the triple dipper got me' 53.

## Data caveats

- `follows` is null on every post, so follows per 1k views isn't available; account-level follower deltas are used instead (Zernio has daily follower counts only from Oct 13 for IG A/B).
- IG completion rate comes back 0 for every reel; watch % = avg watch time / duration is used as a proxy.
- Opening and cover are known only for posts made by the pipeline (Oct 12+). Opening is fully confounded with account (A = wipe by rule, B = talk-first), so wipe vs talk can't be separated from audience differences.
- Mack's own native posts (Oct 5–11 mostly) have no opening/cover metadata, and many (the 7–15 s clips) aren't in Dropbox, so their content is inferred from captions only.
- Native vs pipeline is confounded with time: both accounts were coming off the Sep 29–Oct 5 viral run, so Oct 5–11 numbers sit higher for everything.
- 'trial' = isSharedToFeed false. Sharing to followers both adds views and is chosen after a reel does well, so trial vs feed is not a fair test.
- Posts from Oct 18 evening onward are under ~30 h old and still climbing.
- Several approved pipeline reels (e.g. Oct 14 'please send broomstick putter recs', Oct 17 'it's not a bit. it's just hot', Oct 12 'new shirt. same four putt') don't appear in Zernio analytics (deleted or not synced), so they're missing.
- TikTok views/caption mapping to source footage comes from clips/state/inventory.md; TikTok reach is 0 for the newest posts (still syncing).
