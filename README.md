# Abstract

This is Merge Tool Selector Program for TortoiseGit.

If a conflict occurs while using TortoiseGit, you need to merge it with the merge tool.
For simple merging tasks (choose one or both), P4Merge is by far the easiest to use.
On the other hand, for non-simple merging work (such as partially adopting changes), 
I would like to use Emacs, which I usually use.
So, I came up with the idea of setting a tool (merge tool selector) that can be selectively started in the merge tool of TortoiseGit.

In my case, I want to start P4Merge at first, and when I see the diff and decide that a serious merge is necessary, I want to start emacs.

# Example of use

## Start MergeToolSelector

Pressing any button will launch the merge tool.

![MergeToolSelector01.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/201153/088d433a-0b43-85f7-5f77-e01119bb8a7f.png)

## P4Merge

An example of starting P4Merge.

![mts_p4merge01.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/201153/87b6371c-e4f7-81b0-1cb3-5ffe332742b7.png)

## emacs

An example of starting emacs.

![mts_emacs01.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/201153/4cd4e78f-1f01-af78-f244-0c5ee99b505c.png)


# Settings

`mergeToolSelector.bat %base %theirs %mine %merged %bname %tname %yname %mname`

![MergeToolSelectorSetting01.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/201153/5fc621ab-8608-92bd-6a22-20c7503efdbe.png)

# Improvement

- Set the default merge tool (P4Merge in my case) to start automatically, and include a function that allows you to select and start another tool as needed.
- Specify the path of the merge tool in the config file
- Allow other tools to be specified
  - TotoiseGitMerge and WinMerge
- Settings to specify arguments of merge tool
