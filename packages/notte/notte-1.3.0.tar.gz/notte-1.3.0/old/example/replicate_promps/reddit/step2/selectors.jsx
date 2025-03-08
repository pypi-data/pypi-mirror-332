const selectors = {
	0: (
		<button
			rpl=""
			className="w-full button-medium px-[var(--rem14)] button-primary items-center justify-center button inline-flex"
		>
			[interactive, top, highlight:0, div[2]/shreddit-interactable-element/button]
		</button>
	),
	1: (
		<button
			rpl=""
			className="w-full button-medium px-[var(--rem14)] button-primary items-center justify-center button inline-flex"
		>
			[interactive, top, highlight:1, div[2]/shreddit-interactable-element[2]/button]
		</button>
	),
	2: (
		<a
			id="reddit-logo"
			className="no-underline flex items-center"
			href="/"
			aria-label="Home"
			slot="trigger"
		>
			[interactive, top, highlight:2, html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div/faceplate-tracker/faceplate-tooltip/a]
		</a>
	),
	3: (
		<label style={{ "--left-label-position": "0px" }}>
			[interactive, top, highlight:3]
		</label>
	),
	4: (
		<input
			type="text"
			enterKeyHint="search"
			name="q"
			maxLength="128"
			placeholder="Search Reddit"
			autoComplete="off"
			inputMode=""
		/>
	),
	5: (
		<button
			rpl=""
			className="button-medium pl-[var(--rem10)] pr-[var(--rem14)] button-secondary items-center justify-center button inline-flex"
			id="get-app"
		>
			[interactive, top, highlight:5, html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[3]/span[2]/span/faceplate-tracker/rpl-tooltip/faceplate-tracker/activate-feature/button]
		</button>
	),
	6: (
		<a
			rpl=""
			className="px-sm hover:no-underline button-medium px-[var(--rem14)] button-brand items-center justify-center button inline-flex"
			href="https://www.reddit.com/login/"
			id="login-button"
			slot="trigger"
		>
			[interactive, top, highlight:6, html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[3]/span[3]/faceplate-tracker/faceplate-tooltip/a]
		</a>
	),
	7: (
		<button
			rpl=""
			className="min-w-[40px] button-medium px-[var(--rem8)] button-plain icon items-center justify-center button inline-flex"
			id="expand-user-drawer-button"
			slot="trigger"
			type="button"
			aria-haspopup="true"
			aria-expanded="false"
		>
			[interactive, top, highlight:7, html/body/shreddit-app/reddit-header-large/reddit-header-action-items/header/nav/div[3]/div/shreddit-async-loader/faceplate-dropdown-menu/faceplate-tooltip/activate-feature/button]
		</button>
	),
	8: (
		<span
			role="button"
			className="absolute top-[50%] -translate-y-1/2 hidden xs:inline right-[8px] opacity-100 visible"
		>
			[interactive, top, highlight:8, span[2]]
		</span>
	),
	9: (
		<button
			rpl=""
			aria-label="Next"
			className="hidden xs:block shrink-0 button-small px-[var(--rem6)] button-media icon items-center justify-center button inline-flex"
		>
			[interactive, top, highlight:9, span[2]/button]
		</button>
	),
	10: (
		<a
			href="/search/?q=Grimes+AND+Martin&source=trending&cId=36b3c722-985f-4d7f-a355-f80bb5ef692d&iId=62dbae14-94b0-44b4-a801-23c2265bd23d"
			className="block hover:no-underline relative w-[280px]"
		>
			[interactive, top, highlight:10, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker/faceplate-tracker/li/a]
		</a>
	),
	11: (
		<img
			src="https://b.thumbs.redditmedia.com/lh3XYdayDnfF474A_Ro9fBWUViOibSr4BoTpx0ETyvg.png"
			alt="r/nba icon"
			className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background"
			width="24"
			height="24"
			style={{ color: "#264184", background: "#264184", width: "24px", height: "24px" }}
			loading="lazy"
		/>
	),
	12: <a href="/search/?q=%22The+Fantastic+Four%22&source=trending&cId=36b3c722-985f-4d7f-a355-f80bb5ef692d&iId=8e47be79-7742-481f-aa0c-313ad4242824" className="block hover:no-underline relative w-[280px]"> [interactive, top, highlight:12, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[2]/faceplate-tracker/li/a]
	</a>,
	13: (
		<img
			src="https://b.thumbs.redditmedia.com/lh3XYdayDnfF474A_Ro9fBWUViOibSr4BoTpx0ETyvg.png"
			alt="r/nba icon"
			className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background"
			width="24"
			height="24"
			style={{ color: "#264184", background: "#264184", width: "24px", height: "24px" }}
			loading="lazy"
		/>
	),
	14: (
		<img
			src="https://b.thumbs.redditmedia.com/lh3XYdayDnfF474A_Ro9fBWUViOibSr4BoTpx0ETyvg.png"
			alt="r/nba icon"
			className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background"
			width="24"
			height="24"
			style={{ color: "#264184", background: "#264184", width: "24px", height: "24px" }}
			loading="lazy"
		/>
	),
	15: <img src="https://styles.redditmedia.com/t5_2qh0f/styles/communityIcon_0wn0ynky4gc51.png?width=48&height=48&frame=1&auto=webp&crop=48:48,smart&s=6f961f9bde940ce681c5abde0e2768e0449628fd" alt="r/entertainment icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="24" height="24" style={{ color: "#EA0027", background: "#EA0027", width: "24px", height: "24px" }} loading="lazy"> [interactive, top, highlight:15, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[3]/faceplate-tracker/li/a/div/div/div/span/img]
	</a>,
	16: <a href="/search/?q=Jordan+AND+arrested&source=trending&cId=36b3c722-985f-4d7f-a355-f80bb5ef692d&iId=32258a37-af7e-4aa8-b5bc-1c2268477d01" className="block hover:no-underline relative w-[280px]"> [interactive, top, highlight:16, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[4]/faceplate-tracker/li/a]
	</a>,
	17: <img loading="lazy" src="https://preview.redd.it/z0p1d17acp1c1.png?width=320&crop=smart&auto=webp&s=dfc0d7e84e295f18c6a964a0f27bbb225cf98572" srcset="https://preview.redd.it/z0p1d17acp1c1.png?width=320&crop=smart&auto=webp&s=dfc0d7e84e295f18c6a964a0f27bbb225cf98572 320w, https://preview.redd.it/z0p1d17acp1c1.png?width=640&crop=smart&auto=webp&s=6e518778a8c0594b4fc3fb419365bb3ca7389d0f 640w, https://preview.redd.it/z0p1d17acp1c1.png?auto=webp&s=fc841f7d67bb3c57cfa165227671e8e4ce3dba26 1024w" sizes="280px" alt="r/nba - Michael Jordan Son Arrested and Book for DUI and Cocaine Possesion." className="absolute h-100 w-100 pointer-events-none object-cover m-0"> [interactive, top, highlight:17, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[4]/faceplate-tracker/li/a/img]
	</a>,
	18: <img src="https://b.thumbs.redditmedia.com/lh3XYdayDnfF474A_Ro9fBWUViOibSr4BoTpx0ETyvg.png" alt="r/nba icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="24" height="24" style={{ color: "#264184", background: "#264184", width: "24px", height: "24px" }} loading="lazy"> [interactive, top, highlight:18, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[4]/faceplate-tracker/li/a/div/div/div/span/img]
	</a>,
	19: <a href="/search/?q=Apple+AND+Invites&source=trending&cId=36b3c722-985f-4d7f-a355-f80bb5ef692d&iId=0f58873b-b231-4998-8540-6d717ec0a390" className="block hover:no-underline relative w-[280px]"> [interactive, top, highlight:19, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[5]/faceplate-tracker/li/a]
	</a>,
	20: <img loading="lazy" src="https://external-preview.redd.it/introducing-apple-invites-a-new-app-that-brings-people-v0-0aYhIlVUBMlgdnr-kCY8fNBGjUjO6j4x-kY3XIU1GzA.jpg?width=320&crop=smart&auto=webp&s=17a3708a062a886cfc786102c88bb4c097fc8816" srcset="https://external-preview.redd.it/introducing-apple-invites-a-new-app-that-brings-people-v0-0aYhIlVUBMlgdnr-kCY8fNBGjUjO6j4x-kY3XIU1GzA.jpg?width=320&crop=smart&auto=webp&s=17a3708a062a886cfc786102c88bb4c097fc8816 320w, https://external-preview.redd.it/introducing-apple-invites-a-new-app-that-brings-people-v0-0aYhIlVUBMlgdnr-kCY8fNBGjUjO6j4x-kY3XIU1GzA.jpg?width=640&crop=smart&auto=webp&s=fc5d3a0a870c2b460e61634e3986339a37fed60b 640w, https://external-preview.redd.it/introducing-apple-invites-a-new-app-that-brings-people-v0-0aYhIlVUBMlgdnr-kCY8fNBGjUjO6j4x-kY3XIU1GzA.jpg?width=1080&crop=smart&auto=webp&s=4128e7767e9be525e24abbfa2115dc77db75a4e8 1080w, https://external-preview.redd.it/introducing-apple-invites-a-new-app-that-brings-people-v0-0aYhIlVUBMlgdnr-kCY8fNBGjUjO6j4x-kY3XIU1GzA.jpg?auto=webp&s=e2bcf22109232033e4292a00d298a130be0e1afc 1200w" sizes="280px" alt="r/apple - Introducing Apple Invites, a new app that brings people together" className="absolute h-100 w-100 pointer-events-none object-cover m-0"> [interactive, top, highlight:20, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[5]/faceplate-tracker/li/a/img]
	</a>,
	21: <img src="https://styles.redditmedia.com/t5_2qh1f/styles/communityIcon_hw7ic6kwornd1.png?width=48&height=48&frame=1&auto=webp&crop=48:48,smart&s=81500aacc7bbe48ca8488262aaadf0ff6119bc94" alt="r/apple icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="24" height="24" style={{ color: "#646D73", background: "#646D73", width: "24px", height: "24px" }} loading="lazy"> [interactive, top, highlight:21, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[5]/faceplate-tracker/li/a/div/div/div/span/img]
	</a>,
	22: <a href="/search/?q=%22Capcom+Fighting+Collection%22&source=trending&cId=36b3c722-985f-4d7f-a355-f80bb5ef692d&iId=e683c915-2491-40ee-8906-fb1960acd892" className="block hover:no-underline relative w-[280px]"> [interactive, top, highlight:22, html/body/shreddit-app/div/div/div/div/search-dynamic-id-cache-controller/shreddit-gallery-carousel/faceplate-tracker[6]/faceplate-tracker/li/a]
	</a>,
	23: <button rpl="" aria-expanded="false" aria-label="Sort by: Hot" className="text-neutral-content-weak button-small pl-[var(--rem10)] pr-[var(--rem6)] button-plain items-center justify-center button inline-flex" aria-haspopup="true"> [interactive, top, highlight:24, faceplate-tooltip/faceplate-tracker/button]
	</button>,
	24: <button rpl="" aria-expanded="false" aria-label="Sort by: Everywhere" className="text-neutral-content-weak button-small pl-[var(--rem10)] pr-[var(--rem6)] button-plain items-center justify-center button inline-flex" aria-haspopup="true"> [interactive, top, highlight:25, faceplate-tooltip/faceplate-tracker/button]
	</button>,
	25: <button rpl="" aria-expanded="false" aria-label="View: " className="text-neutral-content-weak button-small pl-[var(--rem10)] pr-[var(--rem6)] button-plain items-center justify-center button inline-flex" aria-haspopup="true"> [interactive, top, highlight:26, faceplate-tooltip/faceplate-tracker/button]
	</button>,
	26: <button rpl="" aria-pressed="false" className="group button flex justify-center aspect-square p-0 border-0 button-secondary disabled:text-interactive-content-disabled button-plain inline-flex items-center hover:text-action-upvote focus-visible:text-action-upvote" style={{ height: "var(--size-button-sm-h)" }} upvote=""> [interactive, top, highlight:27, span/span/button]
	</button>,
	27: <button rpl="" aria-pressed="false" className="group button flex justify-center aspect-square p-0 border-0 button-secondary disabled:text-interactive-content-disabled button-plain inline-flex items-center hover:text-action-downvote focus-visible:text-action-downvote" style={{ height: "var(--size-button-sm-h)" }} downvote=""> [interactive, top, highlight:28, span/span/button[2]]
	</button>,
	28: <a rpl="" className="button border-md flex flex-row justify-center items-center h-xl font-semibold relative text-12 button-secondary inline-flex items-center px-sm" data-post-click-location="comments-button" href="/r/MadeMeSmile/comments/1ii230g/it_made_me_smile_when_this_hero_told_tucker/" name="comments-action-button" style={{ height: "var(--size-button-sm-h)", font: "var(--font-button-sm)" }} target="_self"> [interactive, top, highlight:29, a]
	</a>,
	29: <button rpl="" aria-label="Give award, 9 awards given" className="button border-md overflow-visible flex flex-row justify-center items-center h-xl font-semibold relative text-12 button-secondary inline-flex items-center px-sm" style={{ height: "var(--size-button-sm-h)", font: "var(--font-button-sm)" }} type="button"> [interactive, top, highlight:30, ]
	</button>,
	30: (
		<img
			alt=""
			className="relative"
			src="https://www.redditstatic.com/marketplace-assets/v1/core/awards/helpful_v1_40.png"
			width="16"
			height="16"
		/>
	),
	31: (
		<button
			rpl=""
			className="button border-md flex flex-row justify-center items-center h-xl font-semibold relative text-12 button-secondary inline-flex items-center px-sm"
			style={{ height: "var(--size-button-sm-h)", font: "var(--font-button-sm)" }}
			type="button"
			aria-haspopup="true"
			aria-expanded="false"
		>
			[interactive, top, highlight:32, button]
		</button>
	),
	32: (
		<a
			rpl=""
			className="text-neutral-content whitespace-nowrap flex items-center h-xl a cursor-pointer text-12 font-semibold no-visited no-underline hover:no-underline"
			data-testid="subreddit-name"
			href="/r/MadeMeSmile/"
			aria-haspopup="dialog"
			aria-expanded="false"
		>
			[interactive, top, highlight:33, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article/shreddit-post/span/span/span/shreddit-async-loader/faceplate-hovercard/a]
		</a>
	),
	33: (
		<img
			src="https://styles.redditmedia.com/t5_2uqcm/styles/communityIcon_kfqpkjbvpv001.png?width=48&height=48&frame=1&auto=webp&crop=48:48,smart&s=871296ce8664f6ad7c584164a1c901a823641c56"
			alt="r/MadeMeSmile icon"
			className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background flex items-center justify-center nd:w-lg nd:h-lg text-16"
			width="24"
			height="24"
			style={{ color: "#0079D3", background: "#0079D3", width: "24px", height: "24px" }}
			loading="lazy"
		/>
	),
	34: (
		<button
			className="button-primary button-x-small button join-btn leading-none h-[24px]"
			data-post-click-location="join"
		>
			[interactive, top, highlight:35]
		</button>
	),
	35: (
		<button
			rpl=""
			aria-label="Open user actions"
			className="button-small px-[var(--rem6)] button-plain icon items-center justify-center button inline-flex"
			aria-haspopup="true"
			aria-expanded="false"
		>
			[interactive, top, highlight:36, faceplate-dropdown-menu/button]
		</button>
	),
	36: (
		<img
			id="post-image"
			alt="r/MadeMeSmile - It made me smile when this hero told Tucker Carlson to stop licking Putin's ass today."
			className="i18n-post-media-img preview-img media-lightbox-img max-h-[100vw] h-full w-full object-contain relative"
			loading="eager"
			fetchpriority="high"
			src="https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?width=640&crop=smart&auto=webp&s=24a8c48561a3927d10555427a35d547afa219e6d"
			srcset="https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?width=320&crop=smart&auto=webp&s=ccd3f3269ef52d33745c28838b686c4ee8f43ef8 320w, https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?width=640&crop=smart&auto=webp&s=24a8c48561a3927d10555427a35d547afa219e6d 640w, https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?auto=webp&s=3936cc33d5b39256c6c4d00db66e586ccfd5f430 901w"
			sizes="(min-width: 1415px) 750px, (min-width: 768px) 50vw, 100vw"
		/>
	),
	37: (
		<a
			data-ks-id="t3_1ii1wyj"
			slot="full-post-link"
			className="absolute inset-0"
			href="/r/Damnthatsinteresting/comments/1ii1wyj/in_1928s_steamboat_bill_jr_buster_keaton/"
			target="_self"
		>
			[interactive, top, highlight:38, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article[2]/shreddit-post/a]
		</a>
	),
	38: (
		<a
			rpl=""
			className="text-neutral-content whitespace-nowrap flex items-center h-xl a cursor-pointer text-12 font-semibold no-visited no-underline hover:no-underline"
			data-testid="subreddit-name"
			href="/r/Damnthatsinteresting/"
			aria-haspopup="dialog"
			aria-expanded="false"
		>
			[interactive, top, highlight:39, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article[2]/shreddit-post/span/span/span/shreddit-async-loader/faceplate-hovercard/a]
		</a>
	),
	39: (
		<img
			src="https://b.thumbs.redditmedia.com/b19-jQLBsVc2-EQfPx5WEQkYIL_clR0mhba4-pHT0AA.png"
			alt="r/Damnthatsinteresting icon"
			className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background flex items-center justify-center nd:w-lg nd:h-lg text-16"
			width="24"
			height="24"
			style={{ color: "#349E48", background: "#349E48", width: "24px", height: "24px" }}
			loading="lazy"
		/>
	),
	40: <a href="/r/Damnthatsinteresting/comments/1ii1wyj/in_1928s_steamboat_bill_jr_buster_keaton/" id="post-title-t3_1ii1wyj" slot="title" className="block font-semibold text-neutral-content-strong m-0 visited:text-neutral-content-weak text-16 xs:text-18 mb-2xs xs:mb-xs overflow-hidden" aria-describedby="feed-post-credit-bar-t3_1ii1wyj"> [interactive, top, highlight:41, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article[2]/shreddit-post/a[2]]
	</a>,
	41: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/DestinyTheGame" style={{ paddingRight: "16px" }}> [interactive, top, highlight:42, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li/a]
	</a>,
	42: <img src="https://styles.redditmedia.com/t5_2vq0w/styles/communityIcon_6f0n71jeeund1.jpg?format=pjpg&s=0b228651a1d0caf2241281300910cd54db502e27" alt="r/DestinyTheGame icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:43, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li/a/span/span/span/img]
	</a>,
	43: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/anime" style={{ paddingRight: "16px" }}> [interactive, top, highlight:44, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[2]/a]
	</a>,
	44: <img src="https://styles.redditmedia.com/t5_2qh22/styles/communityIcon_18jg89hnk9ae1.png" alt="r/anime icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:45, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[2]/a/span/span/span/img]
	</a>,
	45: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/destiny2" style={{ paddingRight: "16px" }}> [interactive, top, highlight:46, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[3]/a]
	</a>,
	46: <img src="https://styles.redditmedia.com/t5_2we4j/styles/communityIcon_k5n4c7i07t4d1.png" alt="r/destiny2 icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:47, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[3]/a/span/span/span/img]
	</a>,
	47: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/FortNiteBR" style={{ paddingRight: "16px" }}> [interactive, top, highlight:48, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[4]/a]
	</a>,
	48: <img src="https://styles.redditmedia.com/t5_3oeyf/styles/communityIcon_rrdzpsn8g94e1.png" alt="r/FortNiteBR icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:49, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[4]/a/span/span/span/img]
	</a>,
	49: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/dndnext" style={{ paddingRight: "16px" }}> [interactive, top, highlight:50, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[5]/a]
	</a>,
	50: <img src="https://styles.redditmedia.com/t5_2vbgl/styles/communityIcon_47xlywkzsy7b1.png" alt="r/dndnext icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:51, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[5]/a/span/span/span/img]
	</a>,
	51: <button rpl="" className="button-small px-[var(--rem10)] button-plain items-center justify-center button inline-flex" data-see-less-label="See less" data-see-more-label="See more" id="popular-communities-list-see-more"> [interactive, top, highlight:52, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/button]
	</button>,
	52: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.redditinc.com/policies/content-policy"> [interactive, top, highlight:53, html/body/shreddit-app/div/div/div[2]/div/div/span/span/faceplate-tracker/a]
	</a>,
	53: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.reddit.com/policies/privacy-policy"> [interactive, top, highlight:54, html/body/shreddit-app/div/div/div[2]/div/div/span/span[2]/faceplate-tracker/a]
	</a>,
	54: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.redditinc.com/policies/user-agreement"> [interactive, top, highlight:55, html/body/shreddit-app/div/div/div[2]/div/div/span/span[3]/faceplate-tracker/a]
	</a>,
	55: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.redditinc.com/policies/impressum"> [interactive, top, highlight:56, html/body/shreddit-app/div/div/div[2]/div/div/span/span[4]/faceplate-tracker/a]
	</a>,
	56: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://redditinc.com"> [interactive, top, highlight:57, html/body/shreddit-app/div/div/div[2]/div/div/span/span[5]/a]
	</a>,
	57: <button rpl="" className="bg-neutral-background shadow-xs button-small px-[var(--rem6)] button-bordered icon items-center justify-center button inline-flex" id="flex-nav-collapse-button"> [interactive, top, highlight:58, html/body/shreddit-app/div/flex-left-nav-container/div/div/rpl-tooltip[2]/button]
	</button>,
	58: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 s:rounded-[8px] no-underline" href="/r/popular/" style={{ paddingRight: "16px" }}> [interactive, top, highlight:59, faceplate-tracker/li/a]
	</a>,
	59: <details open="" className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:60, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details]
	</details>,
	60: <summary aria-controls="TOPICS" aria-expanded="true" className="font-normal"> [interactive, top, highlight:61, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/summary]
	</summary>,
	61: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:62, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper/details]
	</details>,
	62: <summary aria-controls="Internet Culture (Viral)" aria-expanded="false" className="font-normal"> [interactive, top, highlight:63, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper/details/summary]
	</summary>,
	63: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:64, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[2]/details]
	</details>,
	64: <summary aria-controls="Games" aria-expanded="false" className="font-normal"> [interactive, top, highlight:65, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[2]/details/summary]
	</summary>,
	65: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:66, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[3]/details]
	</details>,
	66: <summary aria-controls="Q&As" aria-expanded="false" className="font-normal"> [interactive, top, highlight:67, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[3]/details/summary]
	</summary>,
	67: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:68, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[4]/details]
	</details>,
	68: <summary aria-controls="Technology" aria-expanded="false" className="font-normal"> [interactive, top, highlight:69, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[4]/details/summary]
	</summary>,
	69: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:70, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[5]/details]
	</details>,
	70: <summary aria-controls="Pop Culture" aria-expanded="false" className="font-normal"> [interactive, top, highlight:71, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[5]/details/summary]
	</summary>,
	71: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:72, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[6]/details]
	</details>,
	72: <summary aria-controls="Movies & TV" aria-expanded="false" className="font-normal"> [interactive, top, highlight:73, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[6]/details/summary]
	</summary>,
	73: <button rpl="" aria-controls="left-nav-more-topics" aria-expanded="false" className="ml-xs mt-2xs button-small px-[var(--rem10)] button-plain items-center justify-center button inline-flex"> [interactive, top, highlight:74, button]
	</button>,
	74: <details open="" className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:75, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details]
	</details>,
	75: <summary aria-controls="RESOURCES" aria-expanded="true" className="font-normal"> [interactive, top, highlight:76, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details/summary]
	</summary>,
	34: <button className="button-primary button-x-small button join-btn leading-none h-[24px]" data-post-click-location="join"> [interactive, top, highlight:35, ]
	</button>,
	35: <button rpl="" aria-label="Open user actions" className="button-small px-[var(--rem6)] button-plain icon items-center justify-center button inline-flex" aria-haspopup="true" aria-expanded="false"> [interactive, top, highlight:36, faceplate-dropdown-menu/button]
	</button>,
	36: <img id="post-image" alt="r/MadeMeSmile - It made me smile when this hero told Tucker Carlson to " stop licking Putin's ass" today." className="i18n-post-media-img preview-img media-lightbox-img max-h-[100vw] h-full w-full object-contain relative" loading="eager" fetchpriority="high" src="https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?width=640&crop=smart&auto=webp&s=24a8c48561a3927d10555427a35d547afa219e6d" srcset="https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?width=320&crop=smart&auto=webp&s=ccd3f3269ef52d33745c28838b686c4ee8f43ef8 320w, https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?width=640&crop=smart&auto=webp&s=24a8c48561a3927d10555427a35d547afa219e6d 640w, https://preview.redd.it/it-made-me-smile-when-this-hero-told-tucker-carlson-to-stop-v0-d43k7djl19he1.jpeg?auto=webp&s=3936cc33d5b39256c6c4d00db66e586ccfd5f430 901w" sizes="(min-width: 1415px) 750px, (min-width: 768px) 50vw, 100vw"> [interactive, top, highlight:37, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article/shreddit-post/div/shreddit-aspect-ratio/shreddit-media-lightbox-listener/div/img[2]]
	</a >,
	37: <a data-ks-id="t3_1ii1wyj" slot="full-post-link" className="absolute inset-0" href="/r/Damnthatsinteresting/comments/1ii1wyj/in_1928s_steamboat_bill_jr_buster_keaton/" target="_self"> [interactive, top, highlight:38, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article[2]/shreddit-post/a]
	</a>,
		38: <a rpl="" className="text-neutral-content whitespace-nowrap flex items-center h-xl a cursor-pointer text-12 font-semibold no-visited no-underline hover:no-underline" data-testid="subreddit-name" href="/r/Damnthatsinteresting/" aria-haspopup="dialog" aria-expanded="false"> [interactive, top, highlight:39, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article[2]/shreddit-post/span/span/span/shreddit-async-loader/faceplate-hovercard/a]
		</a>,
			40: <img src="https://b.thumbs.redditmedia.com/b19-jQLBsVc2-EQfPx5WEQkYIL_clR0mhba4-pHT0AA.png" alt="r/Damnthatsinteresting icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background flex items-center justify-center nd:w-lg nd:h-lg text-16" width="24" height="24" style={{ color: "#349E48", background: "#349E48", width: "24px", height: "24px" }} loading="lazy"> [interactive, top, highlight:40, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article[2]/shreddit-post/span/span/span/shreddit-async-loader/faceplate-hovercard/a/div/img]
			</a>,
				41: <a href="/r/Damnthatsinteresting/comments/1ii1wyj/in_1928s_steamboat_bill_jr_buster_keaton/" id="post-title-t3_1ii1wyj" slot="title" className="block font-semibold text-neutral-content-strong m-0 visited:text-neutral-content-weak text-16 xs:text-18 mb-2xs xs:mb-xs overflow-hidden" aria-describedby="feed-post-credit-bar-t3_1ii1wyj"> [interactive, top, highlight:41, html/body/shreddit-app/div/div/div[2]/main/shreddit-feed/article[2]/shreddit-post/a[2]]
				</a>,
					42: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/DestinyTheGame" style={{ paddingRight: "16px" }}> [interactive, top, highlight:42, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li/a]
					</a>,
						43: <img src="https://styles.redditmedia.com/t5_2vq0w/styles/communityIcon_6f0n71jeeund1.jpg?format=pjpg&s=0b228651a1d0caf2241281300910cd54db502e27" alt="r/DestinyTheGame icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:43, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li/a/span/span/span/img]
						</a>,
							44: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/anime" style={{ paddingRight: "16px" }}> [interactive, top, highlight:44, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[2]/a]
							</a>,
								45: <img src="https://styles.redditmedia.com/t5_2qh22/styles/communityIcon_18jg89hnk9ae1.png" alt="r/anime icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:45, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[2]/a/span/span/span/img]
								</a>,
									46: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/destiny2" style={{ paddingRight: "16px" }}> [interactive, top, highlight:46, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[3]/a]
									</a>,
										47: <img src="https://styles.redditmedia.com/t5_2we4j/styles/communityIcon_k5n4c7i07t4d1.png" alt="r/destiny2 icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:47, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[3]/a/span/span/span/img]
										</a>,
											48: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/FortNiteBR" style={{ paddingRight: "16px" }}> [interactive, top, highlight:48, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[4]/a]
											</a>,
												49: <img src="https://styles.redditmedia.com/t5_3oeyf/styles/communityIcon_rrdzpsn8g94e1.png" alt="r/FortNiteBR icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:49, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[4]/a/span/span/span/img]
												</a>,
													50: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 no-underline" href="/r/dndnext" style={{ paddingRight: "16px" }}> [interactive, top, highlight:50, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[5]/a]
													</a>,
														51: <img src="https://styles.redditmedia.com/t5_2vbgl/styles/communityIcon_47xlywkzsy7b1.png" alt="r/dndnext icon" className="mb-0 shreddit-subreddit-icon__icon rounded-full overflow-hidden nd:visible nd:bg-secondary-background" width="32" height="32" style={{ width: "32px", height: "32px" }} loading="lazy"> [interactive, top, highlight:51, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/li[5]/a/span/span/span/img]
														</a>,
															52: <button rpl="" className="button-small px-[var(--rem10)] button-plain items-center justify-center button inline-flex" data-see-less-label="See less" data-see-more-label="See more" id="popular-communities-list-see-more"> [interactive, top, highlight:52, html/body/shreddit-app/div/div/div[2]/div/aside[2]/aside/div/li/ul/button]
															</button>,
																53: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.redditinc.com/policies/content-policy"> [interactive, top, highlight:53, html/body/shreddit-app/div/div/div[2]/div/div/span/span/faceplate-tracker/a]
																</a>,
																	54: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.reddit.com/policies/privacy-policy"> [interactive, top, highlight:54, html/body/shreddit-app/div/div/div[2]/div/div/span/span[2]/faceplate-tracker/a]
																	</a>,
																		55: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.redditinc.com/policies/user-agreement"> [interactive, top, highlight:55, html/body/shreddit-app/div/div/div[2]/div/div/span/span[3]/faceplate-tracker/a]
																		</a>,
																			56: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://www.redditinc.com/policies/impressum"> [interactive, top, highlight:56, html/body/shreddit-app/div/div/div[2]/div/div/span/span[4]/faceplate-tracker/a]
																			</a>,
																				57: <a rpl="" className="a cursor-pointer text-secondary-plain-weak hover:text-secondary-plain-hover no-visited visited:text-secondary-plain-weak text-12 no-visited hover:underline" href="https://redditinc.com"> [interactive, top, highlight:57, html/body/shreddit-app/div/div/div[2]/div/div/span/span[5]/a]
																				</a>,
																					58: <button rpl="" className="bg-neutral-background shadow-xs button-small px-[var(--rem6)] button-bordered icon items-center justify-center button inline-flex" id="flex-nav-collapse-button"> [interactive, top, highlight:58, html/body/shreddit-app/div/flex-left-nav-container/div/div/rpl-tooltip[2]/button]
																					</button>,
																						59: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary-onBackground bg-neutral-background-selected hover:bg-neutral-background-selected hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 s:rounded-[8px] no-underline" href="/r/popular/" style={{ paddingRight: "16px" }}> [interactive, top, highlight:59, faceplate-tracker/li/a]
																						</a>,
																							60: <details open="" className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:60, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details]
																							</details>,
																								61: <summary aria-controls="TOPICS" aria-expanded="true" className="font-normal"> [interactive, top, highlight:61, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/summary]
																								</summary>,
																									62: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:62, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper/details]
																									</details>,
																										63: <summary aria-controls="Internet Culture (Viral)" aria-expanded="false" className="font-normal"> [interactive, top, highlight:63, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper/details/summary]
																										</summary>,
																											64: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:64, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[2]/details]
																											</details>,
																												65: <summary aria-controls="Games" aria-expanded="false" className="font-normal"> [interactive, top, highlight:65, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[2]/details/summary]
																												</summary>,
																													66: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:66, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[3]/details]
																													</details>,
																														67: <summary aria-controls="Q&As" aria-expanded="false" className="font-normal"> [interactive, top, highlight:67, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[3]/details/summary]
																														</summary>,
																															68: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:68, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[4]/details]
																															</details>,
																																69: <summary aria-controls="Technology" aria-expanded="false" className="font-normal"> [interactive, top, highlight:69, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[4]/details/summary]
																																</summary>,
																																	70: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:70, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[5]/details]
																																	</details>,
																																		71: <summary aria-controls="Pop Culture" aria-expanded="false" className="font-normal"> [interactive, top, highlight:71, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[5]/details/summary]
																																		</summary>,
																																			72: <details className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:72, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[6]/details]
																																			</details>,
																																				73: <summary aria-controls="Movies & TV" aria-expanded="false" className="font-normal"> [interactive, top, highlight:73, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-expandable-section-helper[6]/details/summary]
																																				</summary>,
																																					74: <button rpl="" aria-controls="left-nav-more-topics" aria-expanded="false" className="ml-xs mt-2xs button-small px-[var(--rem10)] button-plain items-center justify-center button inline-flex"> [interactive, top, highlight:74, button]
																																					</button>,
																																						75: <details open="" className="p-0 m-0 bg-transparent border-none rounded-none"> [interactive, top, highlight:75, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details]
																																						</details>,
																																							76: <summary aria-controls="RESOURCES" aria-expanded="true" className="font-normal"> [interactive, top, highlight:76, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details/summary]
																																							</summary>,
																																								77: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 s:rounded-[8px] bg-transparent no-underline" href="https://www.redditinc.com" style={{ paddingRight: "16px" }}> [interactive, top, highlight:77, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-tracker/li/a]
																																								</a>,
																																									78: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 s:rounded-[8px] bg-transparent no-underline" href="https://accounts.reddit.com/adsregister?utm_source=web3x_consumer&utm_name=left_nav_cta&utm_content=default" style={{ paddingRight: "16px" }}> [interactive, top, highlight:78, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-tracker[2]/li/a]
																																									</a>,
																																										79: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 s:rounded-[8px] bg-transparent no-underline" href="https://support.reddithelp.com/hc?utm_source=reddit&utm_medium=footer&utm_campaign=evergreen" style={{ paddingRight: "16px" }}> [interactive, top, highlight:79, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-tracker[3]/li/a]
																																										</a>,
																																											80: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 s:rounded-[8px] bg-transparent no-underline" href="https://redditblog.com/" style={{ paddingRight: "16px" }}> [interactive, top, highlight:80, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-tracker[4]/li/a]
																																											</a>,
																																												81: <a className="flex justify-between relative px-md gap-[0.5rem] text-secondary hover:text-secondary-hover active:bg-interactive-pressed hover:bg-neutral-background-hover hover:no-underline cursor-pointer py-2xs -outline-offset-1 s:rounded-[8px] bg-transparent no-underline" href="https://www.reddit.com/topics/a-1/" style={{ paddingRight: "16px" }}> [interactive, top, highlight:81, html/body/shreddit-app/div/flex-left-nav-container/div/div[2]/reddit-sidebar-nav/nav/nav/faceplate-expandable-section-helper/details/faceplate-auto-height-animator/div/faceplate-tracker[9]/li/a]
																																												</a>,
																																													82: <a href="https://www.google.com/intl/en/policies/privacy/" target="_blank"> [interactive, top, highlight:86, html/body/div[2]/div[3]/div[2]/a]
																																													</a>,
																																														83: <a href="https://www.google.com/intl/en/policies/terms/" target="_blank"> [interactive, top, highlight:87, html/body/div[2]/div[3]/div[2]/a[2]]
	}
