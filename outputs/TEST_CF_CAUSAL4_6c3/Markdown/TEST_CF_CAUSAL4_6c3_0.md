
# Parameters

    Name :                      TEST_CF_CAUSAL4_6c3-0
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
    Cf convert :                6
    Counterfacts :              3
    Topn :                      7
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      62204154868 function calls (61877459785 primitive calls) in 82516.90 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 82516.902 82516.902 {built-in method builtins.exec}
                      1    4.824    4.824 82516.902 82516.902 <string>:1(<module>)
                      1  193.820  193.820 82512.079 82512.079 main.py:95(CFagent)
                2742926 2025.775    0.001 24070.189    0.009 agent.py:217(counterfact)
                8228778   33.586    0.000 20590.446    0.003 agent.py:29(learn)
                2742926   13.160    0.000 16769.861    0.006 game.py:41(step)
                8228760  523.046    0.000 16735.791    0.002 learner.py:42(Qlearn)
                2742926   16.325    0.000 16133.597    0.006 layers.py:710(step)
        363060910/36367518 1491.640    0.000 11982.337    0.000 module.py:866(_call_impl)
               28138758   77.102    0.000 11312.276    0.000 network.py:24(forward)
              106907324 11300.972    0.000 11300.972    0.000 {built-in method tensor}
              100537534   56.467    0.000 11174.688    0.000 game.py:37(board)
               28138758  366.368    0.000 11049.679    0.000 container.py:117(forward)
                2742926  252.908    0.000 10223.993    0.004 layers.py:17(step)
              273637564  822.641    0.000 9946.790    0.000 layer.py:98(move)
                2742926  305.245    0.000 8002.820    0.003 agent.py:54(_learn)
                2742926  301.938    0.000 7349.317    0.003 agent.py:209(_learn)
                8228760   70.507    0.000 6580.985    0.001 optimizer.py:84(wrapper)
                9953609  267.836    0.000 6465.745    0.001 agent.py:49(__call__)
              109717050 3585.390    0.000 6410.098    0.000 layer.py:151(update)
                8228760   36.612    0.000 6259.811    0.001 grad_mode.py:24(decorate_context)
                8228760  263.886    0.000 6143.352    0.001 adam.py:55(step)
                4470555   94.471    0.000 6141.746    0.001 agent.py:172(choose_action)
                2742927  428.456    0.000 5870.192    0.002 layers.py:676(update)
              273637564  926.399    0.000 5827.594    0.000 layers.py:727(check)
                8228760 1294.536    0.000 5588.373    0.001 _functional.py:53(adam)
                2742926   85.410    0.000 5186.422    0.002 agent.py:117(_learn)
                2742926 2608.852    0.001 4593.996    0.002 replaybuffer.py:28(teleporter_save_data)
                8228760   33.641    0.000 4288.714    0.001 tensor.py:195(backward)
                2742926 3301.494    0.001 4285.880    0.002 replaybuffer.py:22(sample_data)
                8228760   34.707    0.000 4253.715    0.001 __init__.py:68(backward)
               56277516  129.453    0.000 4079.912    0.000 conv.py:398(forward)
                8228760 4054.578    0.000 4054.578    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               56277516   79.255    0.000 3891.405    0.000 conv.py:390(_conv_forward)
               56277516 3812.150    0.000 3812.150    0.000 {built-in method conv2d}
                2742926 2860.243    0.001 3712.816    0.001 replaybuffer.py:49(sample_data)
                2742926 1896.875    0.001 3681.092    0.001 agent.py:88(interveen)
               78930422  164.009    0.000 3098.850    0.000 linear.py:93(forward)
               78930422   66.130    0.000 2854.498    0.000 functional.py:1737(linear)
               78930422 2772.867    0.000 2772.867    0.000 {built-in method torch._C._nn.linear}
              273527259  532.614    0.000 2759.656    0.000 layers.py:721(isFree)
             2348308090 1846.920    0.000 2227.042    0.000 layer.py:95(isFree)
                2742926 1382.189    0.001 2078.840    0.001 agent.py:67(modify)
              182649184 1835.923    0.000 1835.923    0.000 {built-in method clone}
              107069180   84.243    0.000 1655.221    0.000 activation.py:713(forward)
               12696535   79.401    0.000 1641.758    0.000 agent.py:59(modify_board)
               42868631 1619.158    0.000 1619.158    0.000 {built-in method cat}
              107069180   92.252    0.000 1570.978    0.000 functional.py:1364(leaky_relu)
             1052395525 1488.077    0.000 1488.077    0.000 layer.py:146(elements)
              107069180 1459.915    0.000 1459.915    0.000 {built-in method torch._C._nn.leaky_relu}
             5376239256  987.644    0.000 1410.169    0.000 enum.py:646(__hash__)
              279757029  303.479    0.000 1328.946    0.000 {built-in method builtins.any}
                2742908   48.642    0.000 1257.535    0.000 agent.py:168(__call__)
                4470555 1045.859    0.000 1216.849    0.000 agent.py:183(convert_values)
                2742926   47.241    0.000 1202.167    0.000 agent.py:112(__call__)
              153603496 1092.060    0.000 1092.060    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12696535 1070.979    0.000 1070.979    0.000 {built-in method torch._C._nn.one_hot}
              273637564  805.447    0.000 1064.031    0.000 layers.py:71(check)
                2764450   35.172    0.000 1060.186    0.000 layers.py:731(restart)
              274292700  134.824    0.000 1055.053    0.000 {built-in method builtins.all}
             2986810750  849.195    0.000 1025.467    0.000 layers.py:692(<genexpr>)
                8228760  174.848    0.000  965.453    0.000 optimizer.py:189(zero_grad)
              153603496  961.840    0.000  961.840    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              273637564  597.859    0.000  957.581    0.000 layers.py:240(check)
             1410372044  379.258    0.000  955.371    0.000 layers.py:682(<genexpr>)
              273637564  526.946    0.000  876.392    0.000 layers.py:280(check)
        12552344305/12552344302  774.407    0.000  849.019    0.000 {built-in method builtins.len}
                2742926   62.970    0.000  773.198    0.000 replaybuffer.py:18(stacker)
                2764450   16.435    0.000  747.244    0.000 level.py:8(__init__)
                2742908   55.834    0.000  649.648    0.000 replaybuffer.py:45(stacker)
                9953609  241.534    0.000  644.761    0.000 exploration.py:53(softmaxer)
               76801748  637.552    0.000  637.552    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             6543971369  635.381    0.000  635.381    0.000 layer.py:91(positions)
                2764450   97.967    0.000  604.028    0.000 levels.py:199(generate)
                2742926  246.623    0.000  592.558    0.000 replaybuffer.py:55(CF_save_data)
              273637564  426.064    0.000  563.210    0.000 layers.py:56(check)
               76801748  555.324    0.000  555.324    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              274292700  344.028    0.000  514.812    0.000 layers.py:107(isDone)
               76801748  514.219    0.000  514.219    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               76801748  512.013    0.000  512.013    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              273637564  328.782    0.000  501.862    0.000 layers.py:267(check)
              273637564  313.932    0.000  487.972    0.000 layers.py:307(check)
              537612320  364.867    0.000  453.340    0.000 tensor.py:906(grad)
               11014752  172.120    0.000  451.086    0.000 random.py:315(sample)
                2742926  251.981    0.000  426.383    0.000 collector.py:53(collect)
              198088627  425.213    0.000  425.213    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             5376270647  422.531    0.000  422.531    0.000 {built-in method builtins.hash}
              109717050  419.229    0.000  419.229    0.000 layer.py:163(<listcomp>)
                5528900   47.801    0.000  410.683    0.000 level.py:41(notUsed)
               76801748  380.149    0.000  380.149    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              273637564  257.354    0.000  376.705    0.000 layers.py:42(check)
                8228760   12.035    0.000  359.148    0.000 loss.py:527(forward)
                8228760   32.776    0.000  347.113    0.000 functional.py:2898(mse_loss)
              109717050  345.290    0.000  345.290    0.000 layer.py:164(<listcomp>)
                8228779  332.886    0.000  332.886    0.000 {built-in method nonzero}
              262531468  244.395    0.000  324.198    0.000 layer.py:126(remove)
               56277516   41.483    0.000  275.866    0.000 flatten.py:39(forward)
               27644500   40.124    0.000  268.224    0.000 layer.py:69(restart)
               82287780  251.639    0.000  251.639    0.000 agent.py:236(<listcomp>)
              417370870  175.071    0.000  242.162    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 9505793: <TEST_CF_CAUSAL4_6c3_0> in cluster <dcc> Done

Job <TEST_CF_CAUSAL4_6c3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  9 00:44:40 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  9 02:36:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 02:36:11 2021
Terminated at Sat Apr 10 01:31:35 2021
Results reported at Sat Apr 10 01:31:35 2021

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

    CPU time :                                   82309.33 sec.
    Max Memory :                                 8539 MB
    Average Memory :                             5997.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7845.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   82523 sec.
    Turnaround time :                            89215 sec.

The output (if any) is above this job summary.

