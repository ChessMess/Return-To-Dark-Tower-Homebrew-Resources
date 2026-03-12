"""
Download images for Return to Dark Tower Designer Diary posts.
Run this script from your local machine.

No external dependencies required (uses Python stdlib only).

Usage:
    python3 download_images.py
"""

import os
import time
import urllib.request
import urllib.error

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "images")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Referer": "https://www.kickstarter.com/",
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
}

_KS = "https://i.kickstarter.com/assets"
_CF = "https://d15chbti7ht62o.cloudfront.net/assets"


def ks(path, v, sig, q=92):
    """Build a signed Kickstarter CDN image URL."""
    return f"{_KS}/{path}?fit=scale-down&origin=ugc&q={q}&v={v}&width=700&sig={sig}"


# Signed image URLs collected directly from the rendered Kickstarter pages.
# Kickstarter CDN images require a signature parameter; unsigned URLs return 404.
# Cloudfront video thumbnails (_h264_*.jpg) are public and need no signature.
POSTS = {
    "post_2731596_alliances_rob_daviau": [
        ks("027/762/540/dbd34fe5d4fcbae67f66c20a556e7644_original.jpg",
           "1579113038", "ZWrUZWGSHzkmuM5RyBd7w4q1j48DQKZEhedAMvRnTic%3D"),
        ks("027/762/548/05f05139772d5a78b68a170a741c5451_original.jpg",
           "1579113087", "Da0E9iKgL1BLdOsyljunJ%2F6q4Zux%2FB99lQlptuhl1wg%3D"),
        ks("027/762/992/7a3b97641df9ca0663652e8516370377_original.jpg",
           "1579115837", "WbrGjaIEbEZwG6ljzYsPEDnG1Cx88cCr8PLCQT%2BFP70%3D"),
        ks("027/762/568/378e9f8ab18e0b14111c8dbcb6251b01_original.jpg",
           "1579113276", "ziS59vQo6obYY%2FTQHQOUWdWBwUEmVJkuawkMJyv4%2BQc%3D"),
        ks("027/762/570/641727894af9c6f7928bd1811ae65caa_original.jpg",
           "1579113292", "wCV7efCVJh6Cphxf%2FbZgrN2fcii6Y%2B%2Ft%2Bn7yPhpxNTs%3D"),
        ks("027/762/582/f9cc664c72f5f06ab5c191a11cab1cea_original.jpg",
           "1579113372", "MHGV%2Fw94vrNSsVyY7W3yyfMOhvgmtpE2uwjKco5lF7Q%3D"),
    ],

    "post_2735575_8_stages_of_grief_tim_burrell_saward": [
        # Cloudfront video thumbnails (public, no signature needed)
        f"{_CF}/027/819/033/323ff1d1c77ea80fcdaa52f59bff3693_h264_base.jpg",
        f"{_CF}/027/819/069/c94a0cdc42d39488fa07e42274fd90ba_h264_high.jpg",
        f"{_CF}/027/819/106/0df10df01daced09681f879f2213cc6f_h264_high.jpg",
        f"{_CF}/027/819/117/0a0e6c0b29a0068f5673fabee27ba07a_h264_high.jpg",
        f"{_CF}/027/819/143/dabd4f5622e9381fcf03fcffef35aa42_h264_base.jpg",
        f"{_CF}/027/819/162/27df478570735ffc6f3240f8601771c2_h264_high.jpg",
        # Signed Kickstarter CDN images
        ks("027/819/128/1b29259f453aacf1b0c0204f1a12115b_original.JPG",
           "1579622073", "FkpFfDs5YYlNmuK301nKlgm5yt%2FFHzh6QP5aqqOoBOM%3D"),
        ks("027/819/175/0826f9f410d2744799f2f3b6ddb0b7f3_original.jpg",
           "1579622269", "gS9H20IOY4AotRH2OoEU%2Bz2lOOFBE8uC%2FJH79ckAEHc%3D"),
        ks("027/819/177/c79daa5c6304ec020a07b83af55cd9ea_original.jpg",
           "1579622297", "ysGjZhL1xFyriBUR%2B4HAENaMw0x8l93qoe2lo7hJmtw%3D"),
        ks("027/819/180/4a8d6148b3fe6b2d8cf90117d2c50e73_original.jpg",
           "1579622329", "stXEAXvC5eYEww%2FVO4p2PpVaKFkIJN5zTeXFDuKU8mc%3D"),
        ks("027/819/201/d8ab1bfee8e5b3d9344319634cbf6b62_original.jpg",
           "1579622433", "b9j9A0NgxSpcfDHvdBRRkgCAxbwvBtyHirworG%2Fq%2BNk%3D"),
    ],

    "post_2737463_dungeons_and_deals_brian_neff": [
        ks("027/843/374/f9e2a3e90fefb1b9121aa15af25d9658_original.jpg",
           "1579807764", "kDvm2NSmlEIqddGOXnmZ9%2FZVnIreMH1GsaXD9i9ZEPM%3D"),
        ks("027/843/068/5c4117a5d91b845868ceac0cb90a331b_original.jpg",
           "1579805604", "vzQ1o24xEMRYjd85rkj%2BMip24I8vVWbu5brm5ULEdXY%3D"),
        ks("027/843/151/cba0bece7f554cf0bea797e35a4c64f7_original.jpg",
           "1579806226", "LZ7RFZvObdgpwkQ8hbjybGJwCfUcWosK6M38p3unlbU%3D"),
    ],

    "post_2742751_ready_for_its_close_up_tim_burrell_saward": [
        ks("027/912/665/9e8b54e2e94843a58d3ff2036b2a9308_original.jpg",
           "1580400114", "eLKkz1pbzdXzPK%2BMdo%2BZaKgo5eHyTd%2BYRnJHFnb2Bqg%3D"),
        ks("027/912/692/f704c9be1d0b0a8017c4b0423e94b9ab_original.jpg",
           "1580400216", "4AhSqSKpZLub2T%2FtcmW4t9sLLJtBrxDPvK3H3DNrxPg%3D"),
        ks("027/912/724/2365b116e101b181b719cf92a4ca1342_original.jpg",
           "1580400365", "nxXnTwfqcT23k8IRqvgrdkP%2B3bIQb2ziKQWSDzUOJIw%3D"),
        ks("027/912/732/ca5a13aff6ea5c05eb58ef7707650288_original.jpg",
           "1580400413", "rVXMZKLe9q%2Bevpv71pZnfSdrahtyJGrQ%2FDLnnUsHPqQ%3D"),
        ks("027/912/750/4a5e3d595a4f83af94aa61cafd253a98_original.jpg",
           "1580400515", "tZlib02wEaHEUkuD%2BbqAXkeiAS%2FKfVPKAhmZP%2B9sNqA%3D"),
        ks("027/912/768/2a695401fc1f761a1e8907145c8c8f02_original.jpg",
           "1580400613", "gTcSHNlPR2bxUOkhNzErTvRy2jv2msjsCmhLTRPtS8Y%3D"),
        ks("027/912/790/72b63c43ba3c4b77693e6f8121a3f951_original.jpg",
           "1580400715", "QMBA40K%2B1tWP0w4ATSKhfGMEW1b5LSwRsnzzuiaB85A%3D"),
        ks("027/912/807/73f581a3140798c2ba135c7c47bca80a_original.jpg",
           "1580400777", "wyIzAdC3Kf8aOL4qRAv8qrbrCvQ9qFLcGWlqL0JR3BM%3D"),
        ks("027/912/815/1b83167255cd5bd319f71eff48a87774_original.jpg",
           "1580400809", "zpb77xJM2UWfpmZOhRBe7lbsSMz9s%2FNexnhJJiYgcnY%3D"),
        ks("027/912/833/9a6dfc8daf4c79afa9fd5ebb8faca0ca_original.jpg",
           "1580400872", "MTHcSOkQBbU3cH%2FMZ9slq7Qe5TNevq669j%2B0TvfHJFY%3D"),
        ks("027/912/849/e083daf50357423c67b77f86bf91c7fb_original.jpg",
           "1580400945", "IN50ydCFUIjrNLRhXiEhgr5t8JdLXsYyLt2uPFQqcZA%3D"),
        ks("027/912/877/59919082819d67136f5dd48298c19ab1_original.jpg",
           "1580401063", "pLNAXSAgE95A7bM0PeGumPOor4q4rmgQFr9A2xAK%2B%2FY%3D"),
    ],

    "post_2745371_feast_for_the_eyes_jason_taylor": [
        ks("027/945/001/c1d654a1a865a6e030595bcbf50c1ba4_original.jpg",
           "1580667286", "GPLjiY%2FbLGFbSTzlrunSWumhrFNlAAVUj0C14zb6CSc%3D"),
        ks("027/945/089/2d9816fc9a21785ed383a4d5fe061fc3_original.jpg",
           "1580668052", "%2BivP6bVspffbZlPleT4MDIEGy%2Bpg9j%2FlRPew2Vp%2FnJk%3D"),
        ks("027/945/140/482ae46fbf765dfd177e091f3c2ebf61_original.jpg",
           "1580668478", "AG88vHmdd7plvwc8tQa6Abtukd%2BZk4eHxIuyxgUkLAQ%3D"),
        ks("027/945/240/da3f1b878596fc753ced718a67df5d3e_original.jpg",
           "1580669087", "PpTg%2BjX53Uh0fGRga%2FAD2T%2FbYsSRNJQLuPj7tsWh%2Bgs%3D"),
        ks("027/945/305/7998750a94221b8e79453375708ed9b7_original.jpg",
           "1580669675", "Up8L%2BNAiajWI8KUp%2B%2BzihnJdx9%2B455qAEBZ8RnHL2JU%3D"),
        ks("027/945/313/87fa5f54bc225b8c2be429eb5988c62c_original.jpg",
           "1580669697", "SHL8JRrEuNqYZPaI4zXolPTfSpHD9jd9ga4gBk59vGw%3D"),
        ks("027/945/323/aa3efdc32f33dd786b46f2375adfda71_original.jpg",
           "1580669832", "BxPCPnSwHCpSjbtSmhvWQxt3CY0llp9e380Z1hOmfDg%3D"),
        ks("027/945/326/10f70cbb39c3b01c0311a30cb0d8a21f_original.jpg",
           "1580669856", "htUOEMEf1nZFwBoiteiBfkTXNVwnxL4ie2Xd1dt%2FjPc%3D"),
        ks("027/945/334/b3f9db5091624adb17906be5fee075b6_original.jpg",
           "1580669902", "NL28E7YTRzGReJTJomtlcdk7MGjvyOWyDhv7Fwni5nQ%3D"),
        ks("027/945/338/8fec7d76c83a41ad942ce665574a733c_original.jpg",
           "1580669937", "XzMsIkTH0oHFIWBo49HbPE9lw8JDmgVJD7Ka1%2FfkCys%3D"),
        ks("027/945/392/9556ea5692955c6a5121599a7a67484d_original.jpg",
           "1580670449", "sFPyMTKfU6%2F6TLE97%2FCrMh%2BX4o4%2BDzuH%2FLHPCsUOnBA%3D"),
        ks("027/945/395/e763a7dce8e64f322b0a141f2e336cf3_original.jpg",
           "1580670477", "r%2BIUPUpsCG8%2Fc6%2Ba2cFcv6j0w0FusCSJy4S7o%2FYIwnA%3D"),
        ks("027/945/416/ea82e9e3de35a3a518e64d4cfc7be4fc_original.jpg",
           "1580670588", "Gt5EnE1H23%2BELKGNndfSyxqrwP%2F2L5Rxf%2BeXgW39mPA%3D"),
        ks("027/945/445/f2265a438ff24a1058327e557e183b59_original.jpg",
           "1580670768", "n6lKRtBfOGTC4tkDOnbNxkAjmr3TOxnd5UVLNS7Ngpc%3D"),
    ],

    "post_2870044_beauty_is_more_than_skin_deep_tim_burrell_saward": [
        ks("029/532/211/3e6e2cab3b55287f2adbeb4d1e56282e_original.jpg",
           "1592586391", "NX623djjNp2n88wMrqeylXg9d5ljjePC%2F0CBe7AYpKg%3D"),
        ks("029/532/222/eaa9fd3c47a47591b9995c3c852c7b10_original.jpg",
           "1592586439", "i0RQP3G4px%2BojReb80M8M0rwBtkON%2BJqcmcsPALpvMk%3D"),
        ks("029/532/224/f90de502046455ad050c61a897d11cfb_original.jpg",
           "1592586464", "sgAFu1%2F3%2BU7oxgqvUOIdXev991IsWR2aJtalY5BuGts%3D"),
        ks("029/532/230/f6509fc06a3828d0252de2601b95b88c_original.jpg",
           "1592586512", "0NXdbnpczOfTwMJpE2HMVjWHJ2AdTcboKUruTscATjo%3D"),
        ks("029/532/247/c9bcb95aac80398fc02552b97b5a48e9_original.png",
           "1592586580", "MXpgq4vzFwcz7Y2qMoYMT0yU7zTcklu2nKDXmBw1oHc%3D", q=100),
        ks("029/532/254/755fe263ed00c85e791e71153152a10b_original.jpg",
           "1592586613", "eROX6%2FEHuE2Ueq6DpYKS%2BRTDliH8fs3wOYj4DNi1JSg%3D"),
        ks("029/532/262/6946646bcecaecc6845d86c0742e67b4_original.jpg",
           "1592586654", "hpr6c%2FdqltRiVHS0TIFHTkaZ5%2B%2FSCnPrpxMvOD4vSRA%3D"),
    ],
}


def safe_filename(url):
    """Extract a clean filename from a URL (strips query string)."""
    return url.split("?")[0].split("/")[-1]


def download_file(url, dest_path):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp, open(dest_path, "wb") as f:
        f.write(resp.read())


def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    total_downloaded = 0
    total_skipped = 0
    total_failed = 0

    for folder, urls in POSTS.items():
        folder_path = os.path.join(IMAGES_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"\n📁 {folder}  ({len(urls)} images)")

        for url in urls:
            filename = safe_filename(url)
            dest = os.path.join(folder_path, filename)

            if os.path.exists(dest):
                print(f"  ✓ Already exists: {filename}")
                total_skipped += 1
                continue

            try:
                download_file(url, dest)
                size = os.path.getsize(dest)
                print(f"  ✅ {filename} ({size:,} bytes)")
                total_downloaded += 1
                time.sleep(0.3)  # be polite
            except Exception as e:
                print(f"  ❌ Failed: {filename} — {e}")
                total_failed += 1

    print(f"\n{'='*50}")
    print(f"Done!  Downloaded: {total_downloaded}  |  Skipped: {total_skipped}  |  Failed: {total_failed}")
    if total_failed > 0:
        print("Tip: Some images may require being logged in to Kickstarter.")
        print("     Try opening a post URL in your browser first, then re-run.")


if __name__ == "__main__":
    main()
