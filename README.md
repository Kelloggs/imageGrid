imageGrid
=========

Merges folders of images into one folder containing a single image grid (e.g. for video generation purposes). No rocket sience involved. I just needed something like this very often in the past, thus i decided to share.

Example:
--------
You have 4 folders containing images representing the frames of a video. If you want to merge them such that they are aligned on a 2 x 2 grid, you can use this script as

{{{
python imageGrid 2 2 folder1 folder2 folder3 folder4
}}}

