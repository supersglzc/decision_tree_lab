import dtree_build
import sys

if __name__ == "__main__":
    # fruits with their size and color
    fruits = [
        [4, 'red', 'apple'],
        [4, 'green', 'apple'],
        [1, 'red', 'cherry'],
        [1, 'green', 'grape'],
        [5, 'red', 'apple']
    ]

    tree = dtree_build.buildtree(fruits)
    dtree_build.printtree(tree, '', ["size", "color"])
    print("fruit [2, 'red'] is: ", dtree_build.classify([2, 'red'], tree))
    print("fruit [4.5, 'red'] is: ", dtree_build.classify([4.5, 'red'], tree))
    print("fruit [1.4, 'green'] is: ", dtree_build.classify([1.4, 'green'], tree))

    max_tree_depth = dtree_build.max_depth(tree)
    print("max number of questions="+str(max_tree_depth))
    if len(sys.argv) > 1: # draw option specified
        import dtree_draw_for_regression_tree
        dtree_draw_for_regression_tree.drawtree(tree, jpeg='fruits_dt.jpg')
