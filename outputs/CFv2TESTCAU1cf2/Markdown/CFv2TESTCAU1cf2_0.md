
# Parameters

    Name :                      CFv2TESTCAU1cf2-0
    Main :                      CFagentv2
    Level :                     Levels.Causal1
    Failed actions chance :     0.0
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000
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
    Counterfacts :              2
    Topn :                      5
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      31076199615 function calls (30902003707 primitive calls) in 57314.93 seconds

##    Ordered by: cumulative time
   List reduced from 518 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57314.926 57314.926 {built-in method builtins.exec}
                      1    5.589    5.589 57314.926 57314.926 <string>:1(<module>)
                      1  172.604  172.604 57309.336 57309.336 main.py:103(CFagentv2)
                6014124   25.088    0.000 18000.080    0.003 agent.py:29(learn)
                6011627  453.319    0.000 14968.590    0.002 learner.py:42(Qlearn)
                8016334   70.670    0.000 7728.581    0.001 optimizer.py:84(wrapper)
        198435498/24241302  870.026    0.000 7609.700    0.000 module.py:866(_call_impl)
                2004708   10.846    0.000 7604.317    0.004 game.py:41(step)
                8016334   34.023    0.000 7404.288    0.001 grad_mode.py:24(decorate_context)
                8016334  232.452    0.000 7295.988    0.001 adam.py:55(step)
                2004708   14.028    0.000 7175.985    0.004 layers.py:719(step)
                2004708  205.418    0.000 6938.756    0.003 agent.py:54(_learn)
               16224968  222.823    0.000 6872.602    0.000 container.py:117(forward)
                8016334 1501.363    0.000 6824.394    0.001 _functional.py:53(adam)
                2004708  201.805    0.000 6449.930    0.003 agent.py:202(_learn)
               14143870   40.594    0.000 6361.369    0.000 network.py:24(forward)
                2004708 1684.851    0.001 5443.436    0.003 agent.py:236(counterfact2)
                8016334   32.244    0.000 4668.375    0.001 tensor.py:195(backward)
                8016334   30.612    0.000 4634.921    0.001 __init__.py:68(backward)
                2004708   58.774    0.000 4573.950    0.002 agent.py:117(_learn)
                8016334 4423.566    0.001 4423.566    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2004708 3551.679    0.002 4047.847    0.002 replaybuffer.py:85(sample_data)
                2004708   33.440    0.000 4019.036    0.002 simulator.py:50(learn)
                2004708  221.196    0.000 3985.596    0.002 simulator.py:23(learn)
                2004708  175.103    0.000 3694.652    0.002 layers.py:17(step)
                2004708 2922.575    0.001 3572.659    0.002 replaybuffer.py:22(sample_data)
              200320006  305.127    0.000 3503.202    0.000 layer.py:98(move)
                2004709  291.292    0.000 3448.557    0.002 layers.py:685(update)
                2004708 2727.357    0.001 3358.340    0.002 replaybuffer.py:52(sample_data)
                4048932  109.745    0.000 2972.765    0.001 agent.py:49(__call__)
               34531034   78.612    0.000 2705.089    0.000 conv.py:398(forward)
               34531034   52.006    0.000 2587.744    0.000 conv.py:390(_conv_forward)
               34531034 2535.738    0.000 2535.738    0.000 {built-in method conv2d}
                2004708  971.327    0.000 2409.925    0.001 agent.py:88(interveen)
               28206289 2169.445    0.000 2169.445    0.000 {built-in method tensor}
                2004708 1500.763    0.001 2109.596    0.001 replaybuffer.py:58(CF_save_data)
               23753155   16.340    0.000 2042.588    0.000 game.py:37(board)
                2004708  987.161    0.000 1854.748    0.001 replaybuffer.py:28(teleporter_save_data)
                2004708 1207.859    0.001 1795.272    0.001 agent.py:67(modify)
               38422194   82.164    0.000 1791.187    0.000 linear.py:93(forward)
               24056502 1041.414    0.000 1713.801    0.000 layer.py:167(NoRock_update)
              200320006  490.479    0.000 1680.080    0.000 layers.py:736(check)
               38422194   31.999    0.000 1667.552    0.000 functional.py:1737(linear)
               38422194 1627.424    0.000 1627.424    0.000 {built-in method torch._C._nn.linear}
               34183454 1446.207    0.000 1446.207    0.000 {built-in method cat}
              136270192 1400.925    0.000 1400.925    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              105254538 1375.706    0.000 1375.706    0.000 {built-in method clone}
              200320006  231.985    0.000 1277.299    0.000 layers.py:730(isFree)
                3815804   32.071    0.000 1267.997    0.000 layers.py:741(restart)
              136270192 1217.013    0.000 1217.013    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2004708  890.746    0.000 1109.850    0.001 replaybuffer.py:91(simulator_save_data)
                8016334  177.641    0.000 1090.041    0.000 optimizer.py:189(zero_grad)
               56728260   47.364    0.000 1063.472    0.000 activation.py:713(forward)
             1088384658  889.991    0.000 1045.314    0.000 layer.py:95(isFree)
                2002212   38.111    0.000 1036.337    0.001 agent.py:171(__call__)
               56728260   47.697    0.000 1016.108    0.000 functional.py:1364(leaky_relu)
                3815804   17.746    0.000  981.897    0.000 level.py:8(__init__)
               56728260  958.826    0.000  958.826    0.000 {built-in method torch._C._nn.leaky_relu}
                2004708   37.561    0.000  954.596    0.000 agent.py:112(__call__)
                6053640   41.352    0.000  883.439    0.000 agent.py:59(modify_board)
                3815804   43.576    0.000  826.832    0.000 levels.py:122(generate)
                8134738  774.509    0.000  774.509    0.000 {built-in method torch._C._nn.one_hot}
               68135096  765.872    0.000  765.872    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               14880558  130.355    0.000  745.072    0.000 level.py:41(notUsed)
                2081098    9.544    0.000  681.295    0.000 simulator.py:20(boardforward)
               68135096  668.041    0.000  668.041    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               68135096  630.294    0.000  630.294    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               68135096  621.665    0.000  621.665    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              198659805  136.870    0.000  547.959    0.000 {built-in method builtins.any}
               40531955  520.603    0.000  520.603    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                2004707   35.569    0.000  508.452    0.000 replaybuffer.py:18(stacker)
             2030805930  343.998    0.000  499.716    0.000 enum.py:646(__hash__)
                2002212   36.744    0.000  495.492    0.000 replaybuffer.py:48(stacker)
               68135096  489.967    0.000  489.967    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              200470900   36.573    0.000  445.358    0.000 {built-in method builtins.all}
               11648518  439.193    0.000  439.193    0.000 {built-in method nonzero}
              414410892   85.284    0.000  432.532    0.000 layers.py:691(<genexpr>)
             1376585672  334.890    0.000  411.089    0.000 layers.py:701(<genexpr>)
                2004708  250.309    0.000  404.771    0.000 collector.py:46(collect)
                6014124  155.917    0.000  404.337    0.000 random.py:315(sample)
              476945762  322.844    0.000  397.487    0.000 tensor.py:906(grad)
              584031391  396.039    0.000  396.039    0.000 layer.py:146(elements)
                8016334   11.235    0.000  394.534    0.000 loss.py:527(forward)
                8016334   30.957    0.000  383.300    0.000 functional.py:2898(mse_loss)
                2004707   28.402    0.000  357.424    0.000 replaybuffer.py:81(stacker)
              115391487  355.823    0.000  355.823    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              200470900  237.991    0.000  344.190    0.000 layers.py:114(isDone)
               14880558   11.544    0.000  335.541    0.000 level.py:38(elementsIn)
                4048932  112.314    0.000  317.789    0.000 exploration.py:53(softmaxer)
              200320006  197.416    0.000  314.013    0.000 layers.py:142(check)
        3738193570/3738193566  264.689    0.000  303.368    0.000 {built-in method builtins.len}
              268455247  253.383    0.000  294.314    0.000 layer.py:130(add)
                2004708   53.576    0.000  278.192    0.000 agent.py:277(counterfact_check)
              200320006  191.649    0.000  276.233    0.000 layers.py:49(check)
              200320006  187.604    0.000  275.209    0.000 layers.py:125(check)
                8016334  255.366    0.000  255.366    0.000 {built-in method torch._C._nn.mse_loss}
               22894824   23.470    0.000  246.239    0.000 layer.py:69(restart)
               16037663  231.633    0.000  231.633    0.000 {built-in method sum}
             2634981441  215.914    0.000  215.914    0.000 layer.py:91(positions)
               14880558  107.769    0.000  213.130    0.000 level.py:39(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9511600: <CFv2TESTCAU1cf2_0> in cluster <dcc> Done

Job <CFv2TESTCAU1cf2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 20:13:40 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 20:19:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 20:19:12 2021
Terminated at Tue Apr 13 12:14:35 2021
Results reported at Tue Apr 13 12:14:35 2021

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

    CPU time :                                   57167.16 sec.
    Max Memory :                                 8762 MB
    Average Memory :                             6273.33 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7622.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57324 sec.
    Turnaround time :                            57655 sec.

The output (if any) is above this job summary.

