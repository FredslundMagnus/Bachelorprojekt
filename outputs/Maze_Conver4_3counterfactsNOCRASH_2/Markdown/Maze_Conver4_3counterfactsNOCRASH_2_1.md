
# Parameters

    Name :                      Maze_Conver4_3counterfactsNOCRASH_2-1
    Main :                      Load_Cfagent
    Level :                     Levels.Maze
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Load name :                 Maze_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      60840481801 function calls (60463601632 primitive calls) in 86042.63 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.675 86115.675 {built-in method builtins.exec}
                      1    4.368    4.368 86115.675 86115.675 <string>:1(<module>)
                      1  322.098  322.098 86111.307 86111.307 main.py:109(Load_Cfagent)
                2771173 2708.383    0.001 24478.166    0.009 agent.py:212(counterfact)
                8313519   31.089    0.000 21262.838    0.003 agent.py:29(learn)
                8313519  525.691    0.000 17249.435    0.002 learner.py:42(Qlearn)
                2771173   11.885    0.000 16219.347    0.006 game.py:42(step)
                2771173   17.268    0.000 15625.033    0.006 layers.py:827(step)
        417521037/40643689 1772.071    0.000 14051.422    0.000 module.py:866(_call_impl)
               32330170   91.679    0.000 13324.247    0.000 network.py:28(forward)
               32330170  416.163    0.000 13009.287    0.000 container.py:117(forward)
                6469756  125.534    0.000 9113.848    0.001 agent.py:176(choose_action)
               98541676 8807.883    0.000 8807.883    0.000 {built-in method tensor}
               92428899   58.520    0.000 8694.249    0.000 game.py:38(board)
                2771173  335.397    0.000 8260.748    0.003 agent.py:54(_learn)
                2771173  420.357    0.000 7942.482    0.003 layers.py:793(update)
               12004549  329.175    0.000 7902.054    0.001 agent.py:49(__call__)
                2771173  251.553    0.000 7642.598    0.003 layers.py:17(step)
                2771173  333.128    0.000 7607.305    0.003 agent.py:204(_learn)
              276391546  461.400    0.000 7364.409    0.000 layer.py:106(move)
                8313519   74.621    0.000 6675.016    0.001 optimizer.py:84(wrapper)
                8313519   36.085    0.000 6352.428    0.001 grad_mode.py:24(decorate_context)
                8313519  267.583    0.000 6237.860    0.001 adam.py:55(step)
                8313519 1293.035    0.000 5677.623    0.001 _functional.py:53(adam)
                2771173   90.537    0.000 5344.043    0.002 agent.py:117(_learn)
               88677520 2892.038    0.000 5229.747    0.000 layer.py:175(NoRock_update)
                2771173 4118.921    0.001 5079.874    0.002 replaybuffer.py:22(sample_data)
                2771173 4075.049    0.001 4986.248    0.002 replaybuffer.py:67(sample_data)
               64660340  148.003    0.000 4776.138    0.000 conv.py:398(forward)
               64660340  101.343    0.000 4553.317    0.000 conv.py:390(_conv_forward)
                8313519   28.248    0.000 4524.537    0.001 tensor.py:195(backward)
                8313519   34.796    0.000 4495.054    0.001 __init__.py:68(backward)
               64660340 4451.974    0.000 4451.974    0.000 {built-in method conv2d}
                8313519 4293.398    0.001 4293.398    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2771173 2444.642    0.001 4289.060    0.002 replaybuffer.py:28(teleporter_save_data)
              276391546 1015.487    0.000 4148.258    0.000 layers.py:844(check)
                2771173 2067.395    0.001 3890.897    0.001 agent.py:88(interveen)
                4636189   61.023    0.000 3793.686    0.001 layers.py:849(restart)
               91448164  197.551    0.000 3680.202    0.000 linear.py:93(forward)
               91448164   79.640    0.000 3379.148    0.000 functional.py:1737(linear)
                4636189   37.543    0.000 3297.997    0.001 level.py:8(__init__)
               91448164 3280.400    0.000 3280.400    0.000 {built-in method torch._C._nn.linear}
                6322217  400.978    0.000 2955.810    0.000 levels.py:9(generate)
              276391546  427.813    0.000 2317.083    0.000 layers.py:838(isFree)
                2771173 1435.611    0.001 2139.239    0.001 agent.py:67(modify)
              123778334  106.457    0.000 1963.318    0.000 activation.py:713(forward)
               14775722   90.828    0.000 1913.767    0.000 agent.py:59(modify_board)
             1962041368 1593.796    0.000 1889.270    0.000 layer.py:103(isFree)
                6469756 1614.836    0.000 1861.871    0.000 agent.py:187(convert_values)
              123778334  104.127    0.000 1856.861    0.000 functional.py:1364(leaky_relu)
              179245486 1819.944    0.000 1819.944    0.000 {built-in method clone}
               42487452 1748.338    0.000 1748.338    0.000 {built-in method cat}
              123778334 1730.949    0.000 1730.949    0.000 {built-in method torch._C._nn.leaky_relu}
                2771173 1060.676    0.000 1391.100    0.001 replaybuffer.py:73(CF_save_data)
                2771173   49.860    0.000 1303.752    0.000 agent.py:172(__call__)
             1397385377 1258.538    0.000 1258.538    0.000 layer.py:154(elements)
               14775722 1246.626    0.000 1246.626    0.000 {built-in method torch._C._nn.one_hot}
              276391546  728.846    0.000 1206.834    0.000 layers.py:168(check)
                2771173   45.297    0.000 1195.869    0.000 agent.py:112(__call__)
              155185688 1108.904    0.000 1108.904    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              280794629  260.796    0.000 1099.128    0.000 {built-in method builtins.any}
               13908567  126.180    0.000 1084.643    0.000 level.py:41(notUsed)
              155185688  995.049    0.000  995.049    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             3511741329  683.894    0.000  985.133    0.000 enum.py:646(__hash__)
                8313519  175.882    0.000  981.873    0.000 optimizer.py:189(zero_grad)
              277117300  150.803    0.000  974.919    0.000 {built-in method builtins.all}
                6322217  465.470    0.000  879.208    0.000 levels.py:75(RFS)
             1587410658  460.089    0.000  865.007    0.000 layers.py:799(<genexpr>)
             2452329999  691.397    0.000  838.332    0.000 layers.py:809(<genexpr>)
            11145791554  746.831    0.000  825.839    0.000 {built-in method builtins.len}
               12004549  290.371    0.000  768.668    0.000 exploration.py:53(softmaxer)
                2771173   46.789    0.000  747.338    0.000 replaybuffer.py:18(stacker)
                2771173   45.291    0.000  703.175    0.000 replaybuffer.py:63(stacker)
               77592844  651.683    0.000  651.683    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               77592844  566.311    0.000  566.311    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               22822969  207.418    0.000  538.808    0.000 random.py:315(sample)
               77592844  523.228    0.000  523.228    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              276391546  334.412    0.000  521.505    0.000 layers.py:141(check)
               77592844  519.756    0.000  519.756    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              543149908  364.357    0.000  455.282    0.000 tensor.py:906(grad)
              276391546  299.167    0.000  450.142    0.000 layers.py:48(check)
               13908567   14.020    0.000  449.768    0.000 level.py:38(elementsIn)
             4559428833  449.537    0.000  449.537    0.000 layer.py:99(positions)
              463200109  439.225    0.000  439.225    0.000 level.py:32(inverse)
                2771173  256.853    0.000  434.548    0.000 collector.py:46(collect)
               37089512   55.920    0.000  421.624    0.000 layer.py:77(restart)
              196792381  414.603    0.000  414.603    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              357085930  305.879    0.000  402.318    0.000 layer.py:134(remove)
               77592844  388.883    0.000  388.883    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              276391546  246.769    0.000  383.638    0.000 layers.py:124(check)
                8313519   12.502    0.000  365.894    0.000 loss.py:527(forward)
              612375206  253.317    0.000  361.383    0.000 layer.py:138(add)
                8313519   31.379    0.000  353.393    0.000 functional.py:2898(mse_loss)
               88677520  334.212    0.000  334.212    0.000 layer.py:186(<listcomp>)
               27947774  328.764    0.000  328.764    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               64660340   51.221    0.000  322.907    0.000 flatten.py:39(forward)
              435121350  217.832    0.000  319.959    0.000 random.py:250(_randbelow_with_getrandbits)
              276391546  211.590    0.000  311.792    0.000 layers.py:23(check)
             3511773056  301.244    0.000  301.244    0.000 {built-in method builtins.hash}
                6322217  153.378    0.000  285.821    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632953: <Maze_Conver4_3counterfactsNOCRASH_2_1> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 16:04:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 16:04:12 2021
Terminated at Thu May 13 15:59:35 2021
Results reported at Thu May 13 15:59:35 2021

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

    CPU time :                                   85892.48 sec.
    Max Memory :                                 8735 MB
    Average Memory :                             6076.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7649.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86123 sec.
    Turnaround time :                            87513 sec.

The output (if any) is above this job summary.

