
# Parameters

    Name :                      ReTest16-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67476745663 function calls (67179724216 primitive calls) in 86107.63 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86107.631 86107.631 {built-in method builtins.exec}
                      1    3.833    3.833 86107.631 86107.631 <string>:1(<module>)
                      1  394.724  394.724 86103.798 86103.798 main.py:75(CFagent)
               11135490   39.225    0.000 33151.125    0.003 agent.py:29(learn)
               11134088  824.858    0.000 27556.333    0.002 learner.py:42(Qlearn)
                3711830   18.538    0.000 20481.193    0.006 game.py:41(step)
                3711830   22.920    0.000 19654.129    0.005 layers.py:718(step)
                3711830  337.011    0.000 13578.104    0.004 layers.py:17(step)
              370173889 1279.697    0.000 13210.335    0.000 layer.py:98(move)
                3711830  396.483    0.000 12808.861    0.003 agent.py:54(_learn)
        334142767/37123011 1377.477    0.000 12337.469    0.000 module.py:866(_call_impl)
                3711830  392.305    0.000 11854.253    0.003 agent.py:202(_learn)
               11134088   95.381    0.000 11597.315    0.001 optimizer.py:84(wrapper)
               25988923   70.393    0.000 11495.968    0.000 network.py:24(forward)
               25988923  353.356    0.000 11258.761    0.000 container.py:117(forward)
               11134088   45.674    0.000 11138.579    0.001 grad_mode.py:24(decorate_context)
               11134088  335.043    0.000 10986.973    0.001 adam.py:55(step)
               11134088 2268.188    0.000 10296.468    0.001 _functional.py:53(adam)
                3711830  111.434    0.000 8425.166    0.002 agent.py:117(_learn)
              370173889 1284.615    0.000 8175.016    0.000 layers.py:735(check)
               11134088   47.304    0.000 6979.996    0.001 tensor.py:195(backward)
               11134088   43.356    0.000 6931.086    0.001 __init__.py:68(backward)
               11134088 6635.073    0.001 6635.073    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3711831  530.311    0.000 6020.184    0.002 layers.py:684(update)
                3711830 4397.307    0.001 5602.129    0.002 replaybuffer.py:22(sample_data)
                7414972  197.513    0.000 5426.711    0.001 agent.py:49(__call__)
                3711830 2327.399    0.001 5008.286    0.001 agent.py:88(interveen)
                3711830 3576.092    0.001 4738.380    0.001 replaybuffer.py:52(sample_data)
                3711830  417.455    0.000 4673.779    0.001 agent.py:210(counterfact)
                3711830 2381.692    0.001 4443.534    0.001 replaybuffer.py:28(teleporter_save_data)
               51977846  113.733    0.000 4093.304    0.000 conv.py:398(forward)
               51977846   88.488    0.000 3925.515    0.000 conv.py:390(_conv_forward)
               51977846 3837.028    0.000 3837.028    0.000 {built-in method conv2d}
               43691333 3556.127    0.000 3556.127    0.000 {built-in method tensor}
               51965627 1987.534    0.000 3365.377    0.000 layer.py:151(update)
               35184575   23.673    0.000 3303.184    0.000 game.py:37(board)
               70543109  141.011    0.000 3270.351    0.000 linear.py:93(forward)
                3711830 2083.621    0.001 3165.638    0.001 agent.py:67(modify)
               70543109   57.363    0.000 3059.382    0.000 functional.py:1737(linear)
               70543109 2986.640    0.000 2986.640    0.000 {built-in method torch._C._nn.linear}
              370173889  496.638    0.000 2890.995    0.000 layers.py:729(isFree)
              370173889 1986.341    0.000 2740.722    0.000 layers.py:471(check)
             2490867014 2037.514    0.000 2394.357    0.000 layer.py:95(isFree)
              207834440 2094.404    0.000 2094.404    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              370173889 1532.432    0.000 2081.078    0.000 layers.py:77(check)
               48238092 2000.023    0.000 2000.023    0.000 {built-in method cat}
                3710428   68.714    0.000 1873.532    0.001 agent.py:171(__call__)
              145787515 1869.407    0.000 1869.407    0.000 {built-in method clone}
              207834440 1845.865    0.000 1845.865    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               96532032   76.683    0.000 1778.836    0.000 activation.py:713(forward)
                3711830   65.011    0.000 1766.928    0.000 agent.py:112(__call__)
               96532032   80.592    0.000 1702.153    0.000 functional.py:1364(leaky_relu)
               11126802   81.217    0.000 1638.181    0.000 agent.py:59(modify_board)
             6661404409 1116.373    0.000 1610.977    0.000 enum.py:646(__hash__)
               96532032 1605.127    0.000 1605.127    0.000 {built-in method torch._C._nn.leaky_relu}
               11134088  255.796    0.000 1595.146    0.000 optimizer.py:189(zero_grad)
                1747507   20.598    0.000 1454.941    0.001 layers.py:740(restart)
                1747507   11.529    0.000 1260.811    0.001 level.py:8(__init__)
              373147424  283.453    0.000 1220.787    0.000 {built-in method builtins.any}
                1747507   76.530    0.000 1168.492    0.001 levels.py:262(generate)
              103917220 1146.909    0.000 1146.909    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11126802 1049.649    0.000 1049.649    0.000 {built-in method torch._C._nn.one_hot}
                3711830  854.055    0.000 1049.517    0.000 replaybuffer.py:58(CF_save_data)
               19881331  171.958    0.000 1023.385    0.000 level.py:41(notUsed)
              103917220 1007.995    0.000 1007.995    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              103917220  953.445    0.000  953.445    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              103917220  948.390    0.000  948.390    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3711830   66.557    0.000  944.029    0.000 replaybuffer.py:18(stacker)
              370173889  738.523    0.000  942.854    0.000 layers.py:62(check)
             2955484744  767.845    0.000  937.334    0.000 layers.py:700(<genexpr>)
                3710428   61.041    0.000  910.233    0.000 replaybuffer.py:48(stacker)
              371183100   65.077    0.000  807.363    0.000 {built-in method builtins.all}
              758854395  157.421    0.000  787.599    0.000 layers.py:690(<genexpr>)
             1044530525  785.737    0.000  785.737    0.000 layer.py:146(elements)
                3711830  455.466    0.000  755.877    0.000 collector.py:46(collect)
             8665653035  732.943    0.000  732.943    0.000 layer.py:91(positions)
              103917220  732.354    0.000  732.354    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              371183100  426.384    0.000  623.844    0.000 layers.py:113(isDone)
              727420624  469.343    0.000  582.572    0.000 tensor.py:906(grad)
                7414972  206.126    0.000  577.710    0.000 exploration.py:53(softmaxer)
        7391892691/7391892688  496.724    0.000  566.918    0.000 {built-in method builtins.len}
                3711830   99.748    0.000  543.867    0.000 agent.py:277(counterfact_check)
               11134088   15.975    0.000  532.796    0.000 loss.py:527(forward)
               11134088   40.115    0.000  516.821    0.000 functional.py:2898(mse_loss)
                7423660  187.192    0.000  499.903    0.000 random.py:315(sample)
              160624745  498.868    0.000  498.868    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              370173889  333.494    0.000  495.955    0.000 layers.py:48(check)
             6661446664  494.611    0.000  494.611    0.000 {built-in method builtins.hash}
               19881331   22.772    0.000  449.855    0.000 level.py:38(elementsIn)
               25982810  371.878    0.000  371.878    0.000 {built-in method sum}
              370173889  255.952    0.000  371.629    0.000 layers.py:23(check)
               11134088  341.849    0.000  341.849    0.000 {built-in method torch._C._nn.mse_loss}
              368910595  201.358    0.000  312.103    0.000 layer.py:126(remove)
               11135200  309.235    0.000  309.235    0.000 {built-in method max}
               51977846   34.458    0.000  295.144    0.000 flatten.py:39(forward)
                7423662  294.931    0.000  294.931    0.000 {built-in method nonzero}
               19881331  138.482    0.000  281.732    0.000 level.py:39(<listcomp>)
              895876410  266.798    0.000  266.798    0.000 level.py:32(inverse)
               51977846  260.685    0.000  260.685    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              470583427  182.968    0.000  251.129    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9515523: <ReTest16_0> in cluster <dcc> Done

Job <ReTest16_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 14 15:03:59 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 14 22:43:34 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 22:43:34 2021
Terminated at Thu Apr 15 22:38:49 2021
Results reported at Thu Apr 15 22:38:49 2021

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

    CPU time :                                   85897.47 sec.
    Max Memory :                                 10421 MB
    Average Memory :                             6782.52 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5963.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            113690 sec.

The output (if any) is above this job summary.

