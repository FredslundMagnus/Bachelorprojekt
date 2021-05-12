
# Parameters

    Name :                      Maze_Conver4_3counterfactsNOCRASH-1
    Main :                      CFagent
    Level :                     Levels.Maze
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66473539615 function calls (66075939232 primitive calls) in 86072.52 seconds

##    Ordered by: cumulative time
   List reduced from 518 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.276 86114.276 {built-in method builtins.exec}
                      1    4.212    4.212 86114.276 86114.276 <string>:1(<module>)
                      1  340.644  340.644 86110.065 86110.065 main.py:80(CFagent)
               10209165   38.383    0.000 24502.025    0.002 agent.py:29(learn)
                3403055 1806.037    0.001 22158.307    0.007 agent.py:212(counterfact)
               10209164  613.548    0.000 20000.201    0.002 learner.py:42(Qlearn)
                3403055   13.397    0.000 15942.134    0.005 game.py:42(step)
                3403055   18.504    0.000 15240.111    0.004 layers.py:827(step)
        442075432/44476740 1707.542    0.000 13929.083    0.000 module.py:866(_call_impl)
               34267576   96.469    0.000 13136.772    0.000 network.py:28(forward)
               34267576  426.828    0.000 12816.071    0.000 container.py:117(forward)
              109914081 9617.529    0.000 9617.529    0.000 {built-in method tensor}
                3403055  335.988    0.000 9505.427    0.003 agent.py:54(_learn)
              102088658   53.349    0.000 9457.971    0.000 game.py:38(board)
                3403055  333.497    0.000 8737.792    0.003 agent.py:204(_learn)
                3403055  296.734    0.000 8476.260    0.002 layers.py:17(step)
              339573244  553.278    0.000 8148.874    0.000 layer.py:106(move)
               10209164   83.261    0.000 7986.272    0.001 optimizer.py:84(wrapper)
               10209164   41.797    0.000 7605.192    0.001 grad_mode.py:24(decorate_context)
               12025402  295.265    0.000 7468.776    0.001 agent.py:49(__call__)
               10209164  294.491    0.000 7468.666    0.001 adam.py:55(step)
                5226901   97.878    0.000 6851.690    0.001 agent.py:176(choose_action)
               10209164 1549.578    0.000 6837.344    0.001 _functional.py:53(adam)
                3403056  492.200    0.000 6720.847    0.002 layers.py:793(update)
                3403055  102.840    0.000 6198.930    0.002 agent.py:117(_learn)
              108897752 3041.847    0.000 5658.945    0.000 layer.py:175(NoRock_update)
                3403055 4179.342    0.001 5178.955    0.002 replaybuffer.py:22(sample_data)
               10209164   40.276    0.000 5072.231    0.000 tensor.py:195(backward)
               10209164   38.241    0.000 5030.473    0.000 __init__.py:68(backward)
                3403055 4062.389    0.001 5028.564    0.001 replaybuffer.py:67(sample_data)
               10209164 4795.332    0.000 4795.332    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              339573244 1207.187    0.000 4772.106    0.000 layers.py:844(check)
               68535152  151.036    0.000 4731.853    0.000 conv.py:398(forward)
               68535152   82.261    0.000 4515.956    0.000 conv.py:390(_conv_forward)
               68535152 4433.695    0.000 4433.695    0.000 {built-in method conv2d}
                3403055 1667.389    0.000 3783.126    0.001 agent.py:88(interveen)
               95996618  187.712    0.000 3621.206    0.000 linear.py:93(forward)
               95996618   75.246    0.000 3343.584    0.000 functional.py:1737(linear)
                3403055 1840.648    0.001 3309.842    0.001 replaybuffer.py:28(teleporter_save_data)
               95996618 3248.361    0.000 3248.361    0.000 {built-in method torch._C._nn.linear}
                3403055 1585.023    0.000 2410.251    0.001 agent.py:67(modify)
              339573244  472.143    0.000 2370.346    0.000 layers.py:838(isFree)
                2794183   38.679    0.000 2198.180    0.001 layers.py:849(restart)
               15428457   99.128    0.000 1934.489    0.000 agent.py:59(modify_board)
              130264194  105.714    0.000 1934.302    0.000 activation.py:713(forward)
                2794183   23.236    0.000 1911.898    0.001 level.py:8(__init__)
             2102486363 1606.890    0.000 1898.203    0.000 layer.py:103(isFree)
              130264194  108.941    0.000 1828.588    0.000 functional.py:1364(leaky_relu)
               49459002 1747.220    0.000 1747.220    0.000 {built-in method cat}
                3811016  234.113    0.000 1706.432    0.000 levels.py:9(generate)
              130264194 1699.089    0.000 1699.089    0.000 {built-in method torch._C._nn.leaky_relu}
                3403054   54.854    0.000 1484.343    0.000 agent.py:172(__call__)
              142784820 1429.188    0.000 1429.188    0.000 {built-in method clone}
                3403055   50.893    0.000 1398.746    0.000 agent.py:112(__call__)
             1289367714 1381.184    0.000 1381.184    0.000 layer.py:154(elements)
              339573244  831.940    0.000 1371.362    0.000 layers.py:168(check)
              190571060 1348.294    0.000 1348.294    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5226901 1150.041    0.000 1340.755    0.000 agent.py:187(convert_values)
              347720581  304.775    0.000 1289.711    0.000 {built-in method builtins.any}
               15428457 1259.565    0.000 1259.565    0.000 {built-in method torch._C._nn.one_hot}
              190571060 1199.567    0.000 1199.567    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10209164  204.401    0.000 1159.533    0.000 optimizer.py:189(zero_grad)
                3403055  829.570    0.000 1043.397    0.000 replaybuffer.py:73(CF_save_data)
              340305600  178.547    0.000  995.154    0.000 {built-in method builtins.all}
             3037602753  813.460    0.000  984.936    0.000 layers.py:809(<genexpr>)
             3591492707  657.606    0.000  950.603    0.000 enum.py:646(__hash__)
        13411095669/13411095666  825.320    0.000  910.610    0.000 {built-in method builtins.len}
             1862108572  482.129    0.000  857.290    0.000 layers.py:799(<genexpr>)
               95285530  784.778    0.000  784.778    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3403055   54.817    0.000  754.883    0.000 replaybuffer.py:18(stacker)
               12025402  278.447    0.000  740.126    0.000 exploration.py:53(softmaxer)
                3403054   52.596    0.000  728.435    0.000 replaybuffer.py:63(stacker)
               95285530  673.626    0.000  673.626    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               95285530  629.294    0.000  629.294    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               95285530  628.412    0.000  628.412    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8382549   74.483    0.000  628.110    0.000 level.py:41(notUsed)
              339573244  378.065    0.000  592.011    0.000 layers.py:141(check)
               17222325  209.474    0.000  545.955    0.000 random.py:315(sample)
              666998794  428.099    0.000  531.876    0.000 tensor.py:906(grad)
                3403055  303.938    0.000  514.361    0.000 collector.py:46(collect)
                3811016  268.556    0.000  504.534    0.000 levels.py:75(RFS)
              339573244  340.189    0.000  501.792    0.000 layers.py:48(check)
             5478758881  495.760    0.000  495.760    0.000 layer.py:99(positions)
               95285530  470.209    0.000  470.209    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              339573244  295.944    0.000  448.374    0.000 layers.py:124(check)
               10209164   14.488    0.000  427.566    0.000 loss.py:527(forward)
               10209164   40.192    0.000  413.078    0.000 functional.py:2898(mse_loss)
              108897752  377.310    0.000  377.310    0.000 layer.py:186(<listcomp>)
              339573244  238.778    0.000  354.931    0.000 layers.py:23(check)
              380150454  262.089    0.000  352.681    0.000 layer.py:134(remove)
              161616331  333.631    0.000  333.631    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              108897752  327.230    0.000  327.230    0.000 layer.py:187(<listcomp>)
               68535152   46.496    0.000  317.113    0.000 flatten.py:39(forward)
              536719332  213.988    0.000  298.553    0.000 layer.py:138(add)
             3591531490  293.003    0.000  293.003    0.000 {built-in method builtins.hash}
              436924212  194.358    0.000  285.902    0.000 random.py:250(_randbelow_with_getrandbits)
               68535152  270.618    0.000  270.618    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                8382549    8.605    0.000  256.311    0.000 level.py:38(elementsIn)
              279178846  254.184    0.000  254.184    0.000 level.py:32(inverse)
               10209164  253.780    0.000  253.780    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624179: <Maze_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:16 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:29:17 2021
Terminated at Mon May 10 01:24:37 2021
Results reported at Mon May 10 01:24:37 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85892.28 sec.
    Max Memory :                                 9725 MB
    Average Memory :                             6502.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6659.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            86121 sec.

The output (if any) is above this job summary.

