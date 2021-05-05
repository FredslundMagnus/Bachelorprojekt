
# Parameters

    Name :                      Maze_Conver2-2
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      63799285577 function calls (63468476702 primitive calls) in 86071.43 seconds

##    Ordered by: cumulative time
   List reduced from 517 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.740 86108.740 {built-in method builtins.exec}
                      1    4.336    4.336 86108.740 86108.740 <string>:1(<module>)
                      1  393.634  393.634 86104.405 86104.405 main.py:79(CFagent)
               10937805   40.818    0.000 32648.171    0.003 agent.py:29(learn)
               10937804  821.337    0.000 27180.355    0.002 learner.py:42(Qlearn)
                3645935   17.838    0.000 16714.161    0.005 game.py:41(step)
                3645935   21.838    0.000 15881.620    0.004 layers.py:718(step)
        370527565/39720381 1511.172    0.000 13658.229    0.000 module.py:866(_call_impl)
               28782577   80.355    0.000 12798.955    0.000 network.py:27(forward)
                3645935  383.844    0.000 12604.997    0.003 agent.py:54(_learn)
               28782577  401.235    0.000 12535.001    0.000 container.py:117(forward)
                3645935  383.114    0.000 11663.895    0.003 agent.py:204(_learn)
               10937804   97.544    0.000 11496.976    0.001 optimizer.py:84(wrapper)
               10937804   47.955    0.000 11048.538    0.001 grad_mode.py:24(decorate_context)
               10937804  316.536    0.000 10902.479    0.001 adam.py:55(step)
               10937804 2230.710    0.000 10229.999    0.001 _functional.py:53(adam)
                3645935  297.644    0.000 8846.693    0.002 layers.py:17(step)
              364481666  558.418    0.000 8516.048    0.000 layer.py:98(move)
                3645935  713.546    0.000 8406.891    0.002 agent.py:212(counterfact)
                3645935  111.381    0.000 8314.419    0.002 agent.py:117(_learn)
                3645936  501.693    0.000 6982.739    0.002 layers.py:684(update)
               10937804   44.349    0.000 6783.397    0.001 tensor.py:195(backward)
               10937804   46.230    0.000 6737.483    0.001 __init__.py:68(backward)
               10937804 6447.792    0.001 6447.792    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8905149  238.211    0.000 6436.523    0.001 agent.py:49(__call__)
                3645935 5119.656    0.001 6340.123    0.002 replaybuffer.py:22(sample_data)
                3645935 5118.225    0.001 6302.157    0.002 replaybuffer.py:67(sample_data)
              364481666 1210.573    0.000 4802.376    0.000 layers.py:735(check)
               57565154  127.362    0.000 4532.942    0.000 conv.py:398(forward)
                3645935 1807.816    0.000 4411.283    0.001 agent.py:88(interveen)
               49124777 4376.756    0.000 4376.756    0.000 {built-in method tensor}
               57565154   84.913    0.000 4342.613    0.000 conv.py:390(_conv_forward)
               57565154 4257.700    0.000 4257.700    0.000 {built-in method conv2d}
               40762696   27.821    0.000 4133.132    0.000 game.py:37(board)
               79055861  156.644    0.000 3628.043    0.000 linear.py:93(forward)
                3645935 1850.522    0.001 3472.710    0.001 replaybuffer.py:28(teleporter_save_data)
               79055861   64.883    0.000 3390.363    0.000 functional.py:1737(linear)
               58334968 1877.988    0.000 3376.801    0.000 layer.py:167(NoRock_update)
               79055861 3308.977    0.000 3308.977    0.000 {built-in method torch._C._nn.linear}
                3645935 2033.975    0.001 3092.119    0.001 agent.py:67(modify)
              364481666  509.641    0.000 2696.194    0.000 layers.py:729(isFree)
                1647755   36.572    0.000 2478.965    0.002 agent.py:176(choose_action)
             2482081878 1840.554    0.000 2186.553    0.000 layer.py:95(isFree)
              204172340 2112.803    0.000 2112.803    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               49010429 2107.358    0.000 2107.358    0.000 {built-in method cat}
              107838438   83.909    0.000 2018.961    0.000 activation.py:713(forward)
              107838438   92.578    0.000 1935.053    0.000 functional.py:1364(leaky_relu)
                2655592   35.925    0.000 1919.106    0.001 layers.py:740(restart)
              204172340 1843.625    0.000 1843.625    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3645934   66.607    0.000 1834.680    0.001 agent.py:172(__call__)
              107838438 1823.736    0.000 1823.736    0.000 {built-in method torch._C._nn.leaky_relu}
               12551084   91.032    0.000 1819.037    0.000 agent.py:59(modify_board)
                3645935   62.481    0.000 1721.691    0.000 agent.py:112(__call__)
                2655592   22.056    0.000 1658.254    0.001 level.py:8(__init__)
               10937804  258.431    0.000 1595.736    0.000 optimizer.py:189(zero_grad)
              118947085 1586.064    0.000 1586.064    0.000 {built-in method clone}
                3622037  212.390    0.000 1487.995    0.000 levels.py:9(generate)
              364481666  835.429    0.000 1383.872    0.000 layers.py:168(check)
              364593600  183.313    0.000 1377.010    0.000 {built-in method builtins.all}
              365583944  307.993    0.000 1303.205    0.000 {built-in method builtins.any}
                3645935 1015.678    0.000 1281.161    0.000 replaybuffer.py:73(CF_save_data)
             2204247749  530.721    0.000 1237.097    0.000 layers.py:690(<genexpr>)
               12551084 1151.957    0.000 1151.957    0.000 {built-in method torch._C._nn.one_hot}
              102086170 1144.527    0.000 1144.527    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             3257442072  823.481    0.000  995.212    0.000 layers.py:700(<genexpr>)
             3969625104  700.996    0.000  992.245    0.000 enum.py:646(__hash__)
              102086170  983.985    0.000  983.985    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3645935   68.392    0.000  968.187    0.000 replaybuffer.py:18(stacker)
              102086170  949.446    0.000  949.446    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3645934   66.811    0.000  938.659    0.000 replaybuffer.py:63(stacker)
              102086170  936.490    0.000  936.490    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1172921040  856.600    0.000  856.600    0.000 layer.py:146(elements)
                3645935  450.788    0.000  746.042    0.000 collector.py:46(collect)
              102086170  728.597    0.000  728.597    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8905149  241.851    0.000  660.984    0.000 exploration.py:53(softmaxer)
        8060208340/8060208337  539.579    0.000  615.042    0.000 {built-in method builtins.len}
              364593600  405.016    0.000  607.653    0.000 layers.py:113(isDone)
              714603274  480.412    0.000  592.185    0.000 tensor.py:906(grad)
              364481666  375.788    0.000  591.809    0.000 layers.py:141(check)
             6423366921  575.775    0.000  575.775    0.000 layer.py:91(positions)
               17191536  214.059    0.000  550.838    0.000 random.py:315(sample)
               10937804   16.200    0.000  531.662    0.000 loss.py:527(forward)
               10937804   43.070    0.000  515.462    0.000 functional.py:2898(mse_loss)
                7966776   62.197    0.000  514.554    0.000 level.py:41(notUsed)
              364481666  347.941    0.000  503.653    0.000 layers.py:48(check)
              364481666  304.650    0.000  460.108    0.000 layers.py:124(check)
                3622037  244.936    0.000  457.389    0.000 levels.py:75(RFS)
                1647755  387.181    0.000  444.415    0.000 agent.py:187(convert_values)
              135144103  418.745    0.000  418.745    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              364481666  243.191    0.000  360.675    0.000 layers.py:23(check)
               10937804  338.079    0.000  338.079    0.000 {built-in method torch._C._nn.mse_loss}
               57565154   36.999    0.000  331.942    0.000 flatten.py:39(forward)
               21875610  312.941    0.000  312.941    0.000 {built-in method sum}
                7291872  311.633    0.000  311.633    0.000 {built-in method nonzero}
               10939058  301.276    0.000  301.276    0.000 {built-in method max}
               57565154  294.943    0.000  294.943    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             3969666575  291.256    0.000  291.256    0.000 {built-in method builtins.hash}
              528659996  206.734    0.000  287.765    0.000 layer.py:130(add)
              375453940  197.544    0.000  284.205    0.000 layer.py:126(remove)
              453111997  184.884    0.000  271.538    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579177: <Maze_Conver2_2> in cluster <dcc> Done

Job <Maze_Conver2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:08 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May  1 18:01:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 18:01:17 2021
Terminated at Sun May  2 17:56:33 2021
Results reported at Sun May  2 17:56:33 2021

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

    CPU time :                                   85901.01 sec.
    Max Memory :                                 10459 MB
    Average Memory :                             6861.01 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5925.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86118 sec.
    Turnaround time :                            486745 sec.

The output (if any) is above this job summary.

