
# Parameters

    Name :                      TEST_CF_CAUSAL4_3-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     23.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      64823363928 function calls (64523957017 primitive calls) in 82515.74 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 82515.740 82515.740 {built-in method builtins.exec}
                      1    5.580    5.580 82515.740 82515.740 <string>:1(<module>)
                      1  308.448  308.448 82510.160 82510.160 main.py:95(CFagent)
                9899181   53.860    0.000 26018.135    0.003 agent.py:29(learn)
                9899161  672.694    0.000 20874.410    0.002 learner.py:42(Qlearn)
                3299727   22.532    0.000 20565.351    0.006 game.py:41(step)
                3299727   23.457    0.000 19711.504    0.006 layers.py:710(step)
                3299727  323.016    0.000 12723.254    0.004 layers.py:17(step)
              329667579 1004.201    0.000 12364.933    0.000 layer.py:98(move)
        335354725/35949505 1478.750    0.000 11815.628    0.000 module.py:866(_call_impl)
               26050344   76.936    0.000 10977.666    0.000 network.py:24(forward)
               26050344  387.836    0.000 10712.018    0.000 container.py:117(forward)
                3299727  824.379    0.000 10283.878    0.003 agent.py:217(counterfact)
                3299727  425.894    0.000 10179.525    0.003 agent.py:54(_learn)
                3299727  417.548    0.000 9193.885    0.003 agent.py:209(_learn)
                9899161  100.861    0.000 7956.475    0.001 optimizer.py:84(wrapper)
                9899161   60.078    0.000 7524.777    0.001 grad_mode.py:24(decorate_context)
                9899161  347.623    0.000 7345.470    0.001 adam.py:55(step)
              329667579 1033.743    0.000 7018.604    0.000 layers.py:727(check)
                3299728  515.526    0.000 6928.234    0.002 layers.py:676(update)
                9899161 1549.177    0.000 6641.241    0.001 _functional.py:53(adam)
                3299727  112.294    0.000 6567.203    0.002 agent.py:117(_learn)
                3299727 5166.881    0.002 6455.427    0.002 replaybuffer.py:22(sample_data)
                8067265  275.140    0.000 5769.463    0.001 agent.py:49(__call__)
                3299727 4446.793    0.001 5550.062    0.002 replaybuffer.py:49(sample_data)
                9899161   45.803    0.000 5532.575    0.001 tensor.py:195(backward)
               51427461 5509.277    0.000 5509.277    0.000 {built-in method tensor}
                9899161   57.052    0.000 5485.185    0.001 __init__.py:68(backward)
               43829495   31.084    0.000 5307.721    0.000 game.py:37(board)
                9899161 5201.587    0.001 5201.587    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               65994550 2964.359    0.000 5085.606    0.000 layer.py:151(update)
               52100688  123.913    0.000 4012.175    0.000 conv.py:398(forward)
                3299727 1623.642    0.000 3916.186    0.001 agent.py:88(interveen)
               52100688   92.988    0.000 3825.561    0.000 conv.py:390(_conv_forward)
               52100688 3732.573    0.000 3732.573    0.000 {built-in method conv2d}
                3299727 2162.395    0.001 3698.584    0.001 replaybuffer.py:28(teleporter_save_data)
              329399733  684.141    0.000 3675.428    0.000 layers.py:721(isFree)
             3033624517 2496.430    0.000 2991.286    0.000 layer.py:95(isFree)
               71551578  156.188    0.000 2983.563    0.000 linear.py:93(forward)
               71551578   64.285    0.000 2745.976    0.000 functional.py:1737(linear)
               71551578 2666.875    0.000 2666.875    0.000 {built-in method torch._C._nn.linear}
                3299727 1718.005    0.001 2641.413    0.001 agent.py:67(modify)
                1484484   36.543    0.000 2099.234    0.001 agent.py:172(choose_action)
               47663889 1955.028    0.000 1955.028    0.000 {built-in method cat}
               11366992   97.108    0.000 1648.518    0.000 agent.py:59(modify_board)
                3299707   73.113    0.000 1625.499    0.000 agent.py:168(__call__)
               97601922  101.179    0.000 1567.443    0.000 activation.py:713(forward)
             6088555822 1093.292    0.000 1563.056    0.000 enum.py:646(__hash__)
              330524241  344.405    0.000 1544.662    0.000 {built-in method builtins.any}
              144258527 1490.217    0.000 1490.217    0.000 {built-in method clone}
                3299727   70.955    0.000 1485.711    0.000 agent.py:112(__call__)
               97601922   86.750    0.000 1466.264    0.000 functional.py:1364(leaky_relu)
               97601922 1362.903    0.000 1362.903    0.000 {built-in method torch._C._nn.leaky_relu}
              329667579  994.811    0.000 1303.504    0.000 layers.py:71(check)
             1024582186 1299.815    0.000 1299.815    0.000 layer.py:146(elements)
              184784312 1295.996    0.000 1295.996    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             3599469643  995.431    0.000 1200.258    0.000 layers.py:692(<genexpr>)
              329667579  770.145    0.000 1167.073    0.000 layers.py:240(check)
              184784312 1139.269    0.000 1139.269    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9899161  208.215    0.000 1133.890    0.000 optimizer.py:189(zero_grad)
               11366992 1083.842    0.000 1083.842    0.000 {built-in method torch._C._nn.one_hot}
                2748287   38.606    0.000 1067.703    0.000 layers.py:731(restart)
              329667579  638.330    0.000 1043.601    0.000 layers.py:280(check)
              329972800  182.959    0.000 1016.454    0.000 {built-in method builtins.all}
                3299727   82.530    0.000 1011.204    0.000 replaybuffer.py:18(stacker)
             2067260969  565.102    0.000  873.499    0.000 layers.py:682(<genexpr>)
                3299707   78.118    0.000  838.041    0.000 replaybuffer.py:45(stacker)
              329667579  610.478    0.000  763.890    0.000 layers.py:56(check)
                2748287   17.658    0.000  749.574    0.000 level.py:8(__init__)
               92392156  746.399    0.000  746.399    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7283362291  713.428    0.000  713.428    0.000 layer.py:91(positions)
                3299727  270.349    0.000  674.952    0.000 replaybuffer.py:55(CF_save_data)
               92392156  670.965    0.000  670.965    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               92392156  606.947    0.000  606.947    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               92392156  605.718    0.000  605.718    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8067265  211.450    0.000  602.206    0.000 exploration.py:53(softmaxer)
              329667579  393.408    0.000  594.383    0.000 layers.py:267(check)
        8035306347/8035306344  522.278    0.000  593.328    0.000 {built-in method builtins.len}
                2748287   97.184    0.000  591.873    0.000 levels.py:199(generate)
               12096028  223.807    0.000  579.442    0.000 random.py:315(sample)
              646745176  434.225    0.000  538.215    0.000 tensor.py:906(grad)
              329667579  337.523    0.000  535.092    0.000 layers.py:307(check)
                3299727  307.211    0.000  520.670    0.000 collector.py:53(collect)
                9899161   20.325    0.000  502.619    0.000 loss.py:527(forward)
              329667579  321.486    0.000  487.828    0.000 layers.py:42(check)
                9899161   53.327    0.000  482.294    0.000 functional.py:2898(mse_loss)
             6088593373  469.770    0.000  469.770    0.000 {built-in method builtins.hash}
                9899182  452.724    0.000  452.724    0.000 {built-in method nonzero}
               92392156  442.454    0.000  442.454    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5496574   48.068    0.000  398.599    0.000 level.py:41(notUsed)
                1484484  339.012    0.000  357.768    0.000 agent.py:183(convert_values)
              158925226  339.008    0.000  339.008    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              282042188  211.071    0.000  299.873    0.000 layer.py:126(remove)
               65994550  285.396    0.000  285.396    0.000 layer.py:163(<listcomp>)
                9899161  284.587    0.000  284.587    0.000 {built-in method torch._C._nn.mse_loss}
              446809591  200.409    0.000  280.699    0.000 layer.py:130(add)
              389048648  182.520    0.000  271.680    0.000 random.py:250(_randbelow_with_getrandbits)
               27482870   40.455    0.000  270.021    0.000 layer.py:69(restart)
                9900296  263.580    0.000  263.580    0.000 {built-in method max}
               52100688   40.157    0.000  254.613    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9505789: <TEST_CF_CAUSAL4_3_0> in cluster <dcc> Done

Job <TEST_CF_CAUSAL4_3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  9 00:44:40 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  9 00:45:19 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 00:45:19 2021
Terminated at Fri Apr  9 23:40:44 2021
Results reported at Fri Apr  9 23:40:44 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   82316.51 sec.
    Max Memory :                                 9702 MB
    Average Memory :                             6530.90 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6682.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   82526 sec.
    Turnaround time :                            82564 sec.

The output (if any) is above this job summary.

