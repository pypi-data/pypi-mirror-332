/*
    movelist.c

    This file contains all function definitions of movelist.h
*/

#include "movelist.h"
#include <stdlib.h>
#include "types.h"
#include <stdio.h>

void
MoveList_Init(MoveList* movelist){
    movelist->extra = NULL;
    movelist->last_extra = NULL;
    movelist->len = 0;
}

int MoveList_Append(MoveList* movelist, Move move, PositionInfo pos_info){
    MoveNode* node;
    if (movelist->len < NCH_MOVELIST_SIZE){
        node = movelist->nodes + movelist->len;
    }
    else{
        node = (MoveNode*)malloc(sizeof(MoveNode));
        if (!node) {
            return -1;
        }

        if (movelist->len == NCH_MOVELIST_SIZE) {
            node->prev = NULL;
            movelist->extra = node;
            movelist->last_extra = node;
        } else {
            movelist->last_extra->next = node;
            node->prev = movelist->last_extra;
            movelist->last_extra = node;
        }
    }
    
    node->next = NULL;
    node->move = move;
    node->pos_info = pos_info;
    
    movelist->len++;
    return 0;
}

void MoveList_Pop(MoveList* movelist) {
    movelist->len--;
    if (movelist->len < NCH_MOVELIST_SIZE){
        return;
    }

    MoveNode* node = movelist->last_extra;

    if (movelist->len == NCH_MOVELIST_SIZE) {
        movelist->extra = NULL;
        movelist->last_extra = NULL;
    }
    else{
        movelist->last_extra = node->prev;
        movelist->last_extra->next = NULL;
    }

    free(node);
}

MoveNode*
MoveList_Get(MoveList* movelist, int idx){
    if (idx >= movelist->len)
        return NULL;
    
    if (idx < NCH_MOVELIST_SIZE){
        return movelist->nodes + idx;
    }

    int temp = NCH_MOVELIST_SIZE;
    MoveNode* node = movelist->extra;
    while (temp < idx){
        if (node){
            node = node->next;
            temp++;
        }
        else{
            return NULL;
        }
    }
    
    return node;    
}

void
MoveList_Free(MoveList* movelist){
    if (movelist->extra){
        MoveNode* node;
        while (movelist->last_extra)
        {
            node = movelist->last_extra;
            movelist->last_extra = node->prev;
            free(node);
        }
    }
}

void
MoveList_Reset(MoveList* movelist){
    MoveList_Free(movelist);
    movelist->len = 0;
}

int
MoveList_CopyExtra(const MoveList* src, MoveList* dst){
    if (!src->extra)
        return 0;

    dst->extra = (MoveNode*)malloc(sizeof(MoveNode));
    if (!dst->extra)
        return -1;

    *dst->extra = *src->extra;

    MoveNode* sn = src->extra;
    MoveNode* dn = dst->extra;

    while (sn->next)
    {
        dn->next = (MoveNode*)malloc(sizeof(MoveNode));
        if (dn->next){
            dn->next = NULL;
            goto fail;
        }

        *dn->next = *sn->next;
        dn->next->prev = dn;
        
        sn = sn->next;
        dn = dn->next;
    }
    
    dst->last_extra = dn;
    
    return 0;

    fail:
        MoveNode *temp;
        dn = dst->extra;
        while (dn)
        {
            temp = dn;
            dn = dn->next;
            free(temp);
        }
        
        return -1;
}